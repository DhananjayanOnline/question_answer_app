from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistrations
        fields = "__all__"

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"
