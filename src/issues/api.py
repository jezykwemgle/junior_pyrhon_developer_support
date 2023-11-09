from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from issues.models import Issue, Message

from .permissions import (
    CanCreateMessages,
    IsIssueParticipant,
    RoleIsAdmin,
    RoleIsJunior,
    RoleIsSenior,
)
from .serializers import (
    IssueDetailSerializer,
    IssueListSerializer,
    IssuePostSerializer,
    MessageGetSerializer,
    MessagePostSerializer,
)


class IssueAPISet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueDetailSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [RoleIsJunior]
        elif self.action == "retrieve":
            permission_classes = [IsIssueParticipant]
        elif self.action == "update":
            permission_classes = [RoleIsSenior | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        elif self.action == "create":
            return IssuePostSerializer
        elif self.action == "retrieve":
            return self.serializer_class


class MessageAPI(ListCreateAPIView):
    lookup_field = "issue_id"
    lookup_url_kwarg = "issue_id"
    queryset = Message.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [
                CanCreateMessages & (RoleIsJunior | RoleIsSenior)
            ]
        elif self.request.method == "GET":
            self.permission_classes = [CanCreateMessages | RoleIsAdmin]
        return super(MessageAPI, self).get_permissions()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MessagePostSerializer
        else:
            return MessageGetSerializer
