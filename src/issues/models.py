from django.db import models


class Issue(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    junior_id = models.IntegerField()
    senior_id = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Message(models.Model):
    body = models.TextField()
    issue_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


# class Status(models.Model):
#     STATUSES = [
#         ('OPENED', 'opened'),
#         ('ASSIGNED', 'assigned'),
#         ('CLOSED', 'closed')
#     ]
#     value = models.CharField(max_length=10,
#                              choices=STATUSES,
#                              default='OPENED')
#
#     def __str__(self):
#         return self.value
# class Issue(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     junior = models.ForeignKey(User,
#                                on_delete=models.CASCADE,
#                                related_name='junior_issues')
#     senior = models.ForeignKey(User,
#                                on_delete=models.CASCADE,
#                                null=True,
#                                related_name='senior_issues')
#     status = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
#
# class Message(models.Model):
#     body = models.TextField()
#     issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Message by {self.user} on {self.issue}"
