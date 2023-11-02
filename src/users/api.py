from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserPrivateSerializer, UserPublicSerializer


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        elif self.action == "list" or "retrieve":
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    def get_serializer_class(self):
        if self.action == "create":
            return UserPrivateSerializer
        elif self.action == "list" or self.action == "retrieve":
            return self.serializer_class
        return self.serializer_class
