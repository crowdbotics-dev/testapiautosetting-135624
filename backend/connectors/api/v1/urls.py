from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135624ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135624", Testconnectors135624ViewSet, basename="testconnectors135624"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
