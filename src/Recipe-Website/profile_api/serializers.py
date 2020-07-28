from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile"""

    class Meta:
        model = models.UserProfile
        exclude = ('last_login','is_active','is_admin')
        extra_kwargs = {
            'password': {
                'write_only' : True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create a new User"""
        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user
