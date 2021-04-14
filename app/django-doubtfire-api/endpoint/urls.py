from django.urls import include, path
from django.conf.urls import url
from endpoint.views import enroll_user, validate_recording

urlpatterns = [
    path('enroll', enroll_user),
    path('validate', validate_recording),
    path("up", views.up, name="up"),
]
