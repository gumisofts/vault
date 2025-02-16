from django.urls import path
from vault.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", SecretValueViewsets, basename="secret-values")

urlpatterns = [path("text/<app_number>", get_environmental_variables)] + router.urls
