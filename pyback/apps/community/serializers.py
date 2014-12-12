from rest_framework import serializers

from pyback.apps.community.models import Community


class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'title', 'description', 'type', 'status', 'code', 'ordering', 'created_at')