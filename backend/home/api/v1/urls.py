from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import APP1ViewSet, X1ViewSet, X2ViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("app1", APP1ViewSet)
router.register("x1", X1ViewSet)
router.register("x2", X2ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
