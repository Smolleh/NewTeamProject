from rest_framework.response import Response
from rest_framework import generics, status
from django.db import IntegrityError
from museumApp.permissions import isCurator
from .models import Quiz, Result, Answer, Question
from rest_framework.views import APIView
from .serializers import QuizDesplaySerializer, QuestionWithAnswersSerializer, QuizStartResponseSerializer, SubmitQuizSerializer, QuestionCreateSerializer, AnswerSerializer

class CuratorProtectedView(APIView):
    permission_classes = [isCurator]

#for viewing all the available quizes details
class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDesplaySerializer

#(moderators) for viewing available quizes details and creating new ones
class quizListCreateView(CuratorProtectedView, generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDesplaySerializer
    
# (moderators) for editing a specific quizes details
class QuizEditView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDesplaySerializer

# (moderators) for viewing all questions for a specific quiz,
# creating quiz questions for a specifc quiz, as well as their answers
class QuizQuestionListCreateView(CuratorProtectedView, generics.ListCreateAPIView):
    serializer_class = QuestionCreateSerializer

    #getting all the questions and their answers associated with a specific quiz
    def get_queryset(self):
        return Question.objects.filter(quiz_id=self.kwargs["quiz_id"])

    #creating the Question object and the answers objects
    def perform_create(self, serializer):
        serializer.save(quiz_id=self.kwargs["quiz_id"])
        
#(moderators) edit a specific question
class QuestionEditView(CuratorProtectedView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer

# taking a quiz
class StartQuizView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    
    
    ##gettting all the info needed for the quiz frontend
    def retrieve(self, request, *args, **kwargs):
        quiz = self.get_object()
        
        #check that the user is signed in
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required to start a quiz"}, status=401)

        #checking if the user has already started this quiz
        existing = Result.objects.filter(quiz=quiz, user=request.user).first()
        if existing:
            #if theyve already finished the quiz, do not let them continue
            if existing.completed:
                return Response(
                    {"detail": "You have already attempted this quiz.", "result_id": existing.id},
                    status=400
                )

            #if they have started a quiz but not submitted it, respond with the same payload as they would have 
            #recieved initially when they first started 
            selected_questions = list(Question.objects.filter(id__in=existing.selected_question_ids))
            payload = {
                "result_id": existing.id,
                "quiz_id": quiz.id,
                "quiz_name": quiz.name,
                "topic": quiz.topic,
                "num_questions": quiz.num_questions,
                "passing_score": quiz.passing_score,
                "questions": selected_questions,
            }
            return Response(QuizStartResponseSerializer(payload).data, status=status.HTTP_200_OK)
        
        # pick random questions
        selected_questions = quiz.get_questions()
        selected_ids = []
        for q in selected_questions:
            selected_ids.append(q.id)

        # create Result object and save the selected questions
        result = Result.objects.create(
            quiz=quiz,
            user=request.user,
            score=0,
            completed=False,
            selected_question_ids=selected_ids,
        )


        # what actually gets sent to the frontend
        payload = {
            "result_id": result.id,
            "quiz_id": quiz.id,
            "quiz_name": quiz.name,
            "topic": quiz.topic,
            "num_questions": quiz.num_questions,
            "passing_score": quiz.passing_score,
            "questions": selected_questions
        }
        return Response(QuizStartResponseSerializer(payload).data, status=status.HTTP_200_OK)
    
    
#submitting a completed quiz
class SubmitQuizView(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = SubmitQuizSerializer

    def update(self, request, *args, **kwargs):
        
        #get the previously created result object
        result = self.get_object()

        #check if an attempt has already been submitted
        if result.completed:
            return Response({"detail": "This quiz attempt has already been submitted."}, status=400)

        
        #validate that the Json sent from frontend matches the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #get the selections from the front end as a pythin list of dictionaries
        #format of the dictionaries = {"question_id": 1, "answer_id": 5}
        selections = serializer.validated_data["answers"] 

        
        # get the previously initialized questions for this quiz attempt and the number of them
        selected_q_ids = result.selected_question_ids
        total = len(selected_q_ids)
        
        # checking that questions have been seleted for this quiz attempt
        if total == 0:
            return Response({"detail": "No stored questions for this result."}, status=400)



        # if no answers are submitted:
        if not selections:
            result.score = 0
            result.completed = True
            result.save(update_fields=["score", "completed"])
            return Response(
                {
                    "result_id": result.id,
                    "quiz_id": result.quiz_id,
                    "correct": 0,
                    "answered": 0,
                    "total": total,
                    "score": result.score,

                },
                status=200
            )
            
        #getting the id's of the submitted answers
        submitted_answer_ids = []
        for s in selections:
            submitted_answer_ids.append(s["answer_id"])


        #creating a dictionary that maps from answer ids to answer objects in the database
        answers_by_id = {}
        answers = Answer.objects.filter(id__in=submitted_answer_ids)
        for a in answers:
            answers_by_id[a.id] = a


        
        
        #counting the number of correct answers
        correct = 0
        seen_questions = set()

        for s in selections:
            #getting the answer object
            ans = answers_by_id.get(s["answer_id"])
            
            #checking that the answer exists
            if not ans:
                return Response({"detail": "Invalid answer_id.", "answer_id": s["answer_id"]},status=400)

            #check that the answer belongs to the same question as claimed
            if ans.question_id != s["question_id"]:
                return Response(
            {"detail": "Answer does not belong to given question.","question_id": s["question_id"],"answer_id": s["answer_id"]},status=400)
            #check that the question is part of this attempt
            if s["question_id"] not in set(result.selected_question_ids):
                return Response({"detail": "Question not part of this quiz attempt.","question_id": s["question_id"]},status=400)
            #don't allow multiple answers for one question
            if ans.question_id in seen_questions:
                return Response({"detail": "Multiple answers submitted for same question.","question_id": ans.question_id},status=400)
            
            
            seen_questions.add(ans.question_id)
            if ans.is_correct:
                correct += 1

        #calculating the score
        answered = len(seen_questions)
        score = (correct / total) * 100

        #updating result object
        result.score = score
        result.completed = True
        result.save(update_fields=["score", "completed"])


        return Response(
            {
                "result_id": result.id,
                "quiz_id": result.quiz_id,
                "correct": correct,
                "answered": answered,
                "total": total,
                "score": score,

            },
            status=200
        )
