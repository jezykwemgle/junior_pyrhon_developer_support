from rest_framework import serializers

from issues.models import Issue


class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "body", "status"]


class IssueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "body", "status", "junior", "senior"]


class IssuePostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False, max_length=3)

    class Meta:
        model = Issue
        fields = ["id", "title", "body", "status"]

    def validate(self, attrs):
        attrs["junior"] = self.context["request"].user
        return attrs
