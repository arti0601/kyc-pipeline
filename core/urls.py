from django.urls import path
from .views import *

urlpatterns = [
    path("create/", create_submission),
    path("<int:pk>/update/", update_status),
    path("queue/", reviewer_queue),
]