from rest_framework import serializers
from .models import *
#serializer for answer objects
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "answer_text"]

#
class QuestionWithAnswersSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source="answer_set", many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "answers"]

#serializer for the quiz taking view
class QuizStartResponseSerializer(serializers.Serializer):
    result_id = serializers.IntegerField()
    quiz_id = serializers.IntegerField()
    quiz_name = serializers.CharField()
    topic = serializers.CharField()
    num_questions = serializers.IntegerField()
    passing_score = serializers.IntegerField()
    questions = QuestionWithAnswersSerializer(many=True)
    
#serializer to store a selected answer 
class SelectedAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()

class SubmitQuizSerializer(serializers.Serializer):
    answers = SelectedAnswerSerializer(many =True, required = False, default = list)


class QuizDesplaySerializer(serializers.ModelSerializer):
    exhibit = serializers.PrimaryKeyRelatedField(
        queryset=Exhibit.objects.all()
    )
    exhibit_name = serializers.StringRelatedField(source="exhibit", read_only=True)
    class Meta:
        model = Quiz
        fields = ['id','name', 'topic', 'num_questions', 'passing_score','exhibit', 'exhibit_name']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["answer_text", "is_correct"]


class QuestionCreateSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source="answer_set", many=True)

    class Meta:
        model = Question
        fields = ["id", "quiz", "question_text", "answers"]
        read_only_fields = ["quiz"]

    def create(self, validated_data):
        answers = validated_data.pop("answer_set")
        question = Question.objects.create(**validated_data)

        for answer in answers:
            Answer.objects.create(question=question, **answer)

        return question

    def update(self, instance, validated_data):
        answers = validated_data.pop("answer_set", None)

        instance.question_text = validated_data.get("question_text", instance.question_text)
        instance.save()

        if answers is not None:
            instance.answer_set.all().delete()
            for a in answers:
                Answer.objects.create(question=instance, **a)

        return instance
