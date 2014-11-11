from django.contrib.auth.models import User
from rest_framework import serializers

from pyback.apps.accounts.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('address', 'phone')

class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'user_profile')
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        """
        Call set_password on user object, unless the
        password will be stored in plain text.
        """
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user