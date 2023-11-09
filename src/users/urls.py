from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api import UserAPISet

router = DefaultRouter()
router.register("", UserAPISet, basename="users")

additional_urls = [
    path(
        "activate/",
        UserAPISet.as_view({"post": "activate"}),
        name="activate",
    ),
]

urlpatterns = router.urls + additional_urls
