from django.contrib import admin
from django.urls import path
from .views import test_index, run_code

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", test_index),
    path("rc/", run_code),
]
