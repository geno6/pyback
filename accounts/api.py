from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer


class Accounts(generics.GenericAPIView):
    """
    List all accounts, or create a new one.
    """

    serializer_class = UserSerializer

    def get(self, request):
        """
        List posts
        :param request:
        :return:Response
        """
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        """
        Create post
        :param request:
        :return:Response
        """
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)