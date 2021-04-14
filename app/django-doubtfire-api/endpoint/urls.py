from django.urls import include, path
from django.conf.urls import url
from endpoint.views import enroll_user, validate_recording, up

urlpatterns = [
    path('enroll', enroll_user),
    path('validate', validate_recording),
    path("up", up, name="up"),
]
