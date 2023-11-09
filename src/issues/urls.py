from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import IssueAPISet, MessageAPI

router = DefaultRouter()
router.register("", IssueAPISet, basename="issues")

message_urls = [
    path("<int:issue_id>/messages/", MessageAPI.as_view()),
]

urlpatterns = router.urls + message_urls
