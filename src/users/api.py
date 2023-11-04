from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserPrivateSerializer, UserPublicSerializer


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        elif self.action == "list" or "retrieve":
            return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "create":
            return UserPrivateSerializer
        elif self.action == "list" or self.action == "retrieve":
            return UserPublicSerializer
