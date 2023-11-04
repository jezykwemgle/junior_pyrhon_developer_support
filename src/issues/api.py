from rest_framework.viewsets import ModelViewSet

from issues.models import Issue

from .serializers import (  # noqa
    IssueDetailSerializer,
    IssueListSerializer,
    IssuePostSerializer,
)


class IssueAPISet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueDetailSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        elif self.action == "create":
            return IssuePostSerializer
        elif self.action == "retrieve":
            return self.serializer_class
