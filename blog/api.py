from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class Posts(APIView):
    """
    List all posts, or create a new one.
    """

    def get(self, request):
        """
        List posts
        :param request:
        :return:Response
        """
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        """
        Create post
        :param request:
        :return:Response
        """
        serializer = PostSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)