from django.conf import settings
from django.db import models

from issues.constants import Status


class Issue(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    junior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="junior_issues",
    )
    senior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="senior_issues",
    )
    status = models.CharField(
        max_length=3, default=Status.OPENED, choices=Status.values()
    )

    class Meta:
        db_table = "issues"

    def __str__(self):
        return self.title


class Message(models.Model):
    body = models.TextField()
    issue = models.ForeignKey(
        "issues.Issue", on_delete=models.CASCADE, related_name="messages"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="messages",
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
