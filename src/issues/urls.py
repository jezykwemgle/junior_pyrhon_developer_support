from rest_framework.routers import DefaultRouter

from .api import IssueAPISet

router = DefaultRouter()
router.register("", IssueAPISet, basename="issues")

urlpatterns = router.urls
