from .models import Smack, Comment
from rest_framework import serializers


class SmackCreationSerialization(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=300)

    class Meta:
        model = Smack
        fields = ['title', 'text']


class CommentCreationSerialization(serializers.ModelSerializer):
    body = serializers.CharField(max_length=300)

    class Meta:
        model = Comment
        fields = ['body',]
