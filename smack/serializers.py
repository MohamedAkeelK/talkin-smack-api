from .models import Smack, Comment
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault


class SmackSerializer(serializers.ModelSerializer):
    author = CurrentUserDefault()
    title = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=300)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Smack
        fields = ['author', 'title', 'text', 'created_at', 'updated_at']


class SmackStatusUpdateSerializer(serializers.ModelSerializer):
    author = CurrentUserDefault()
    title = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=300)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Smack
        fields = ['author', 'title', 'text', 'created_at', 'updated_at']


class CommentCreationSerialization(serializers.ModelSerializer):
    body = serializers.CharField(max_length=300)

    class Meta:
        model = Comment
        fields = ['body',]
