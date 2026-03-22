from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from museumApp.models import Exhibit
from .models import Quiz, Question, Answer, Result
from unittest import mock
 
 
class QuizAPITestCase(APITestCase):
 
    def setUp(self):
        """Create test data before each test"""
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
 
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
 
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.quiz1 = Quiz.objects.create(
            name="Quiz One",
            topic="AI Ethics",
            num_questions=5,
            passing_score=60,
            exhibit=self.exhibit
        )
        self.quiz2 = Quiz.objects.create(
            name="Quiz Two",
            topic="Machine Learning",
            num_questions=3,
            passing_score=70,
            exhibit=self.exhibit
        )
 
    def test_get_all_quizzes_success(self):
        """Test retrieving all quizzes from the public list endpoint"""
        response = self.client.get('/quizzes-api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
 
    def test_get_all_quizzes_manage_success(self):
        """Test retrieving all quizzes from the curator manage endpoint"""
        response = self.client.get('/quizzes-api/manage/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
 
    def test_create_quiz_success(self):
        """Test creating a new quiz"""
        data = {
            'name': 'New Quiz',
            'topic': 'Bias in AI',
            'num_questions': 4,
            'passing_score': 75,
            'exhibit': self.exhibit.exhibitId
        }
        response = self.client.post('/quizzes-api/manage/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quiz.objects.count(), 3)
 
    def test_get_single_quiz_manage_success(self):
        """Test retrieving a single quiz via the manage endpoint"""
        response = self.client.get(f'/quizzes-api/manage/{self.quiz1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Quiz One")
 
    def test_get_single_quiz_manage_not_found(self):
        """Test retrieving a non-existent quiz returns 404"""
        response = self.client.get('/quizzes-api/manage/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
    def test_update_quiz_success(self):
        """Test updating an existing quiz"""
        data = {
            'name': 'Updated Quiz',
            'topic': 'Updated Topic',
            'num_questions': 10,
            'passing_score': 80,
            'exhibit': self.exhibit.exhibitId
        }
        response = self.client.put(f'/quizzes-api/manage/{self.quiz1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.quiz1.refresh_from_db()
        self.assertEqual(self.quiz1.name, 'Updated Quiz')
 
    def test_delete_quiz_success(self):
        """Test deleting a quiz"""
        response = self.client.delete(f'/quizzes-api/manage/{self.quiz1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quiz.objects.count(), 1)
 
 
class QuestionAPITestCase(APITestCase):
 
    def setUp(self):
        """Create test data before each test"""
        patcher = mock.patch('museumApp.permissions.isCurator.has_permission', return_value=True)
        self.mock_permission = patcher.start()
        self.addCleanup(patcher.stop)
 
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
 
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz",
            topic="AI Safety",
            num_questions=3,
            passing_score=60,
            exhibit=self.exhibit
        )
        self.question = Question.objects.create(
            question_text="What is AI?",
            quiz=self.quiz
        )
        self.answer_correct = Answer.objects.create(
            answer_text="Artificial Intelligence",
            is_correct=True,
            question=self.question
        )
        self.answer_wrong = Answer.objects.create(
            answer_text="Alien Intelligence",
            is_correct=False,
            question=self.question
        )
 
    def test_get_questions_for_quiz_success(self):
        """Test retrieving all questions for a specific quiz"""
        response = self.client.get(f'/quizzes-api/manage/{self.quiz.id}/questions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
 
    def test_create_question_success(self):
        """Test creating a question with answers for a quiz"""
        data = {
            'question_text': 'What is machine learning?',
            'answers': [
                {'answer_text': 'A subset of AI', 'is_correct': True},
                {'answer_text': 'A type of database', 'is_correct': False}
            ]
        }
        response = self.client.post(
            f'/quizzes-api/manage/{self.quiz.id}/questions/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Answer.objects.count(), 4)
 
    def test_get_single_question_success(self):
        """Test retrieving a single question"""
        response = self.client.get(f'/quizzes-api/manage/question/{self.question.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question_text'], "What is AI?")
 
    def test_get_single_question_not_found(self):
        """Test retrieving a non-existent question returns 404"""
        response = self.client.get('/quizzes-api/manage/question/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
    def test_update_question_success(self):
        """Test updating a question and replacing its answers"""
        data = {
            'question_text': 'Updated question text?',
            'answers': [
                {'answer_text': 'Updated correct answer', 'is_correct': True},
                {'answer_text': 'Updated wrong answer', 'is_correct': False}
            ]
        }
        response = self.client.put(
            f'/quizzes-api/manage/question/{self.question.id}/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.question.refresh_from_db()
        self.assertEqual(self.question.question_text, 'Updated question text?')
 
    def test_delete_question_success(self):
        """Test deleting a question also removes its answers"""
        response = self.client.delete(f'/quizzes-api/manage/question/{self.question.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)
        self.assertEqual(Answer.objects.count(), 0)
 
 
class StartQuizAPITestCase(APITestCase):
 
    def setUp(self):
        """Create test data before each test"""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
 
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz",
            topic="AI Safety",
            num_questions=2,
            passing_score=50,
            exhibit=self.exhibit
        )
        self.question1 = Question.objects.create(question_text="Q1?", quiz=self.quiz)
        self.question2 = Question.objects.create(question_text="Q2?", quiz=self.quiz)
 
        Answer.objects.create(answer_text="A1 correct", is_correct=True, question=self.question1)
        Answer.objects.create(answer_text="A1 wrong", is_correct=False, question=self.question1)
        Answer.objects.create(answer_text="A2 correct", is_correct=True, question=self.question2)
        Answer.objects.create(answer_text="A2 wrong", is_correct=False, question=self.question2)
 
    def test_start_quiz_unauthenticated_fails(self):
        """Test that unauthenticated users cannot start a quiz"""
        response = self.client.get(f'/quizzes-api/{self.quiz.id}/start/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
 
    def test_start_quiz_success(self):
        """Test that an authenticated user can start a quiz"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/quizzes-api/{self.quiz.id}/start/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('result_id', response.data)
        self.assertIn('questions', response.data)
        self.assertEqual(response.data['quiz_name'], "Test Quiz")
        self.assertEqual(Result.objects.count(), 1)
 
    def test_start_quiz_not_found(self):
        """Test starting a non-existent quiz returns 404"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/quizzes-api/9999/start/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
    def test_start_quiz_resumes_in_progress(self):
        """Test that starting a quiz already in progress returns the same result"""
        self.client.force_authenticate(user=self.user)
        first_response = self.client.get(f'/quizzes-api/{self.quiz.id}/start/')
        first_result_id = first_response.data['result_id']
 
        second_response = self.client.get(f'/quizzes-api/{self.quiz.id}/start/')
        self.assertEqual(second_response.status_code, status.HTTP_200_OK)
        self.assertEqual(second_response.data['result_id'], first_result_id)
        self.assertEqual(Result.objects.count(), 1)
 
    def test_start_quiz_already_completed_returns_score(self):
        """Test that starting an already completed quiz returns only the score"""
        self.client.force_authenticate(user=self.user)
        Result.objects.create(
            quiz=self.quiz,
            user=self.user,
            score=80.0,
            completed=True,
            selected_question_ids=[self.question1.id, self.question2.id]
        )
        response = self.client.get(f'/quizzes-api/{self.quiz.id}/start/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('score: ', response.data)
        self.assertEqual(response.data['score: '], 80.0)
 
 
class SubmitQuizAPITestCase(APITestCase):
 
    def setUp(self):
        """Create test data before each test"""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
 
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz",
            topic="AI Safety",
            num_questions=2,
            passing_score=50,
            exhibit=self.exhibit
        )
        self.question1 = Question.objects.create(question_text="Q1?", quiz=self.quiz)
        self.question2 = Question.objects.create(question_text="Q2?", quiz=self.quiz)
 
        self.answer1_correct = Answer.objects.create(
            answer_text="A1 correct", is_correct=True, question=self.question1
        )
        self.answer1_wrong = Answer.objects.create(
            answer_text="A1 wrong", is_correct=False, question=self.question1
        )
        self.answer2_correct = Answer.objects.create(
            answer_text="A2 correct", is_correct=True, question=self.question2
        )
        self.answer2_wrong = Answer.objects.create(
            answer_text="A2 wrong", is_correct=False, question=self.question2
        )
 
        self.result = Result.objects.create(
            quiz=self.quiz,
            user=self.user,
            score=0,
            completed=False,
            selected_question_ids=[self.question1.id, self.question2.id]
        )
 
    def test_submit_quiz_all_correct_success(self):
        """Test submitting a quiz with all correct answers"""
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': self.answer1_correct.id},
                {'question_id': self.question2.id, 'answer_id': self.answer2_correct.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['correct'], 2)
        self.assertEqual(response.data['score'], 100.0)
        self.result.refresh_from_db()
        self.assertTrue(self.result.completed)
 
    def test_submit_quiz_partial_correct_success(self):
        """Test submitting a quiz with only some correct answers"""
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': self.answer1_correct.id},
                {'question_id': self.question2.id, 'answer_id': self.answer2_wrong.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['correct'], 1)
        self.assertEqual(response.data['score'], 50.0)
 
    def test_submit_quiz_empty_answers_success(self):
        """Test submitting a quiz with no answers scores zero"""
        data = {'answers': []}
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['correct'], 0)
        self.assertEqual(response.data['score'], 0)
        self.result.refresh_from_db()
        self.assertTrue(self.result.completed)
 
    def test_submit_quiz_already_submitted_fails(self):
        """Test that resubmitting a completed quiz is rejected"""
        self.result.completed = True
        self.result.score = 100.0
        self.result.save()
 
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': self.answer1_correct.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_submit_quiz_invalid_answer_id_fails(self):
        """Test that submitting a non-existent answer ID is rejected"""
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': 9999}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_submit_quiz_answer_wrong_question_fails(self):
        """Test that submitting an answer belonging to a different question is rejected"""
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': self.answer2_correct.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_submit_quiz_question_not_in_attempt_fails(self):
        """Test that submitting an answer for a question not in this attempt is rejected"""
        outside_question = Question.objects.create(question_text="Outside Q?", quiz=self.quiz)
        outside_answer = Answer.objects.create(
            answer_text="Outside answer", is_correct=True, question=outside_question
        )
        data = {
            'answers': [
                {'question_id': outside_question.id, 'answer_id': outside_answer.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
    def test_submit_quiz_multiple_answers_same_question_fails(self):
        """Test that submitting two answers for the same question is rejected"""
        data = {
            'answers': [
                {'question_id': self.question1.id, 'answer_id': self.answer1_correct.id},
                {'question_id': self.question1.id, 'answer_id': self.answer1_wrong.id}
            ]
        }
        response = self.client.patch(
            f'/quizzes-api/{self.quiz.id}/submit/',
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
 
class QuizAuthenticationTestCase(APITestCase):
 
    def setUp(self):
        """Create test users and quiz data"""
        curator_group, _ = Group.objects.get_or_create(name='Curator')
 
        self.curator_user = User.objects.create_user(username='curator', password='testpass123')
        self.curator_user.groups.add(curator_group)
 
        self.regular_user = User.objects.create_user(username='regularuser', password='testpass123')
 
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            domain="Healthcare",
            backgroundDeploymentContext="Test context",
            intededUse="Test use",
            viewNumber=0
        )
        self.quiz = Quiz.objects.create(
            name="Test Quiz",
            topic="AI Safety",
            num_questions=2,
            passing_score=50,
            exhibit=self.exhibit
        )
 
    def test_unauthenticated_public_quiz_list_succeeds(self):
        """Test that unauthenticated users can view the public quiz list"""
        response = self.client.get('/quizzes-api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_unauthenticated_manage_get_fails(self):
        """Test that unauthenticated GET requests to manage endpoint are rejected"""
        response = self.client.get('/quizzes-api/manage/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
 
    def test_unauthenticated_manage_post_fails(self):
        """Test that unauthenticated POST requests to manage endpoint are rejected"""
        data = {
            'name': 'New Quiz',
            'topic': 'Topic',
            'num_questions': 3,
            'passing_score': 60,
            'exhibit': self.exhibit.exhibitId
        }
        response = self.client.post('/quizzes-api/manage/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
 
    def test_authenticated_curator_manage_get_succeeds(self):
        """Test that an authenticated curator can access the manage endpoint"""
        self.client.force_authenticate(user=self.curator_user)
        response = self.client.get('/quizzes-api/manage/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_authenticated_curator_manage_post_succeeds(self):
        """Test that an authenticated curator can create a quiz"""
        self.client.force_authenticate(user=self.curator_user)
        data = {
            'name': 'Curator Quiz',
            'topic': 'Topic',
            'num_questions': 3,
            'passing_score': 60,
            'exhibit': self.exhibit.exhibitId
        }
        response = self.client.post('/quizzes-api/manage/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
    def test_non_curator_manage_post_denied(self):
        """Test that a non-curator authenticated user cannot create a quiz"""
        self.client.force_authenticate(user=self.regular_user)
        data = {
            'name': 'Sneaky Quiz',
            'topic': 'Topic',
            'num_questions': 3,
            'passing_score': 60,
            'exhibit': self.exhibit.exhibitId
        }
        response = self.client.post('/quizzes-api/manage/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
 
    def test_logout_prevents_manage_access(self):
        """Test that logging out revokes access to the manage endpoint"""
        self.client.force_authenticate(user=self.curator_user)
        response = self.client.get('/quizzes-api/manage/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
        self.client.force_authenticate(user=None)
        response = self.client.get('/quizzes-api/manage/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)