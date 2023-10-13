from django.contrib import admin
from django.urls import path

from users.api import all_issues, all_users, create_issue, create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/all/', all_users),
    path('users/create/', create_user),
    path('issues/all/', all_issues),
    path('issues/create/', create_issue)
]
