from rest_framework import serializers

from issues.models import Issue, Message


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


class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "body", "issue", "user", "timestamp"]
        read_only_fields = ["id", "issue", "user", "timestamp"]

    def validate(self, attrs):
        request = self.context["request"]
        issue_id = request.parser_context["kwargs"]["issue_id"]

        try:
            issue = Issue.objects.get(id=issue_id)
        except Issue.DoesNotExist:
            raise serializers.ValidationError("Issue does not exist")
        attrs["issue"] = issue
        attrs["user"] = request.user
        return attrs


class MessageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "body", "user", "timestamp"]
