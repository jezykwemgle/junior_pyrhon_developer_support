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
