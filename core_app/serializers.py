
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrations
        fields = "__all__"



    
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    created_date = serializers.CharField(read_only=True)
    upvotes=serializers.CharField(read_only=True)
    class Meta:
        model = Answers
        fields = [
            "answer",
            "user",
            "created_date",
            "upvotes",
        ]

    def create(self, validated_data):
        question = self.context.get('question')
        user = self.context.get('user')
        return Answers.objects.create(**validated_data, question=question, user=user)

        # question.answers_set.create(user=user, **validated_data)


class QuestionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user=serializers.CharField(read_only=True)
    question_answer=AnswerSerializer(read_only=True, many=True)
    class Meta:
        model = Questions
        fields = [
            "id",
            "title",
            "describtion",
            "image",
            "user",
            "question_answer",
        ]