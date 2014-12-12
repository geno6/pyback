from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Community

from pyback.apps.community.serializers import CommunitySerializer


class CommunityMixin(object):
    """
    Mixin to inherit from.
    """
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityList(CommunityMixin, ListCreateAPIView):
    """
    Return a list of all the users, or create new ones
    """


class CommunityDetail(CommunityMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific user, update it, or delete it.
    """

    pass