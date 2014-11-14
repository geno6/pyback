from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from pyback.apps.accounts.serializers import UserSerializer


class UserMixin(object):
    """
    Mixin to inherit from.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, ListCreateAPIView):
    """
    Return a list of all the users, or create new ones
    """

    def pre_save(self, obj):
        return 0

    def post_save(self, user, created=False):
        """
        Save user token
        """
        Token.objects.create(user=user)
        return


class UserDetail(UserMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific user, update it, or delete it.
    """

    pass