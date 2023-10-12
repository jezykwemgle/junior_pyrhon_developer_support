from django.db import models


class Role(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Issue(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField()
    junior_id = models.IntegerField()
    senior_id = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Message(models.Model):
    body = models.TextField()
    issue_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.body


# class Role(models.Model):
#     ROLES = [
#         ('ADMIN', 'admin'),
#         ('JUNIOR', 'junior'),
#         ('OPERATOR', 'operator')
#     ]
#     value = models.CharField(max_length=10,
#                              choices=ROLES,
#                              default='JUNIOR')
#
#     def __str__(self):
#         return self.value

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
#
#
# class User(models.Model):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
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
#                                status = models.CharField(max_length=255)
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
