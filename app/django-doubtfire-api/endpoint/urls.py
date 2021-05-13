from django.urls import path
from endpoint.views import (
    enroll_user,
    validate_recording,
    check_redis_health,
    redirect_flower_dashboard,
)

urlpatterns = [
    path("enroll", enroll_user),
    path("validate", validate_recording),
    path("redis-healthcheck", check_redis_health, name="up"),
    path("flower", redirect_flower_dashboard),
]
