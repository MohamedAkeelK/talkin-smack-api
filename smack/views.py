from django.shortcuts import render, get_object_or_404
from .models import Smack, Comment
from rest_framework import generics, status, viewsets
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from .serializers import CommentSerializer

User = get_user_model()


class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SmackView(generics.GenericAPIView):

    serializer_class = serializers.SmackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):

        smack = Smack.objects.all()
        serializer = self.serializer_class(instance=smack, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            print(f"\n {serializer.data}")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmackIdView(generics.GenericAPIView):

    serializer_class = serializers.SmackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, smack_id):
        smack = get_object_or_404(Smack, pk=smack_id)
        serializer = self.serializer_class(instance=smack)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, smack_id):

        smack = get_object_or_404(Smack, pk=smack_id)
        serializer = self.serializer_class(instance=smack, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, smack_id):

        smack = get_object_or_404(Smack, id=smack_id)
        smack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateSmackStatusView(generics.GenericAPIView):

    serializer_class = serializers.SmackStatusUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, smack_id):
        smack = get_object_or_404(Smack, pk=smack_id)
        serializer = self.serializer_class(instance=smack, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class UserSmackView(generics.GenericAPIView):

    serializer_class = serializers.SmackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_id):

        user = User.objects.get(pk=user_id)
        smack = Smack.objects.all().filter(author=user)
        serializer = self.serializer_class(instance=smack, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

# todo : this is not working


class UserSmackDetailView(generics.GenericAPIView):
    serializer_class = serializers.SmackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_id, smack_id):
        user = User.objects.get(pk=user_id)
        smack = Smack.objects.all().filter(author=user).filter(pk=smack_id)
        serializer = self.serializer_class(instance=smack)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


# from django.shortcuts import render, get_object_or_404
# from rest_framework import generics, status
# from rest_framework.response import Response
# from . import serializers
# from .models import Smack
# from rest_framework.permissions import IsAuthenticated
# # Create your views here.


# class HelloSmackView(generics.GenericAPIView):
#     def get(self, request):
#         return Response(data={"message": "Hello smack"}, status=status.HTTP_200_OK)


# class SmackCreateListView(generics.GenericAPIView):

#     serializer_class = serializers.SmackCreationSerialization
#     queryset = Smack.objects.all()
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         smack = Smack.objects.all()
#         serializer = self.serializer_class(instance=smack, many=True)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         user = request.user

#         if serializer.is_valid():
#             serializer.save(author=user)

#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SmackDetailView(generics.GenericAPIView):

#     serializer_class=serializers.SmackDetailSerialization

#     def get(self, request, smack_id):

#         smack = get_object_or_404(Smack, pk=smack_id)

#         serializer = self.serializer_class(instance=smack)

#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, smack_id):
#         data=request.data

#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(data=serializer.data, status = status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, smack_id):
#         pass
