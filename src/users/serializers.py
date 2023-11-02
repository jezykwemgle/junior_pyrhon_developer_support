from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.constants import Role
from users.models import User


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class UserPrivateSerializer(serializers.ModelSerializer):
    role = serializers.CharField(required=False, max_length=2)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "role"]

    def validate_role(self, value):
        if value not in [Role.JUNIOR, Role.SENIOR]:
            raise serializers.ValidationError(
                "Invalid role. Choose either 'junior' or 'senior'."
            )
        return value

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs
