from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Smack
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class HelloSmackView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello smack"}, status=status.HTTP_200_OK)


class SmackCreateListView(generics.GenericAPIView):

    serializer_class = serializers.SmackCreationSerialization
    queryset = Smack.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        smack = Smack.objects.all()
        serializer = self.serializer_class(instance=smack, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(author=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmackDetailView(generics.GenericAPIView):
    def get(self, request, smack_id):
        
        smack = get_object_or_404(Smack, pk=smack_id)

        serializer = self.serializer_class(instance=smack)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, smack_id):
        pass

    def delete(self, request, smack_id):
        pass
