from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer', 'reg_date']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'answers', 'reg_date']

class InterestSerializer(serializers.ModelSerializer):
    percent = serializers.IntegerField()  

    class Meta:
        model = Interest
        fields = ['title', 'quantity', 'percent']

class StudentSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'number', 'interests']