from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ActivationKey, User
from .serializers import UserPrivateSerializer, UserPublicSerializer
from .services import send_activation_email, send_response_email


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = User.objects.get(email=serializer.data["email"])
        activation_key = ActivationKey.objects.create(user=user)

        send_activation_email(serializer.data["email"], activation_key.key)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(
        detail=False,
        methods=["post"],
    )
    def activate(self, request):
        key = request.query_params.get("key")
        try:
            activation_key = ActivationKey.objects.get(key=key)
            user = activation_key.user
            user.is_active = True
            user.save()
            activation_key.delete()
            send_response_email(user.email)
            return Response({"message": "User activated successfully."})
        except ActivationKey.DoesNotExist:
            return Response(
                {"message": "Something went wrong."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_permissions(self):
        if self.action == "create" and self.request.method == "POST":
            return [permissions.AllowAny()]
        elif (
            self.action == "list" or "retrieve"
        ) and self.request.method == "GET":
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

    def get_serializer_class(self):
        if self.action == "create":
            return UserPrivateSerializer
        elif self.action == "list" or self.action == "retrieve":
            return UserPublicSerializer
