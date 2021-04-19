from django.urls import include, path
from django.conf.urls import url
from endpoint.views import enroll_user, validate_recording, redis_healthcheck

urlpatterns = [
    path('enroll', enroll_user),
    path('validate', validate_recording),
    path("redis-healthcheck", redis_healthcheck, name="up"),
]
