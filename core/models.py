from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=20)  # merchant / reviewer

class KYCSubmission(models.Model):
    STATUS_CHOICES = [
        ("draft", "draft"),
        ("submitted", "submitted"),
        ("under_review", "under_review"),
        ("approved", "approved"),
        ("rejected", "rejected"),
        ("more_info_requested", "more_info_requested"),
    ]

    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    submission = models.ForeignKey(KYCSubmission, on_delete=models.CASCADE)
    file = models.FileField(upload_to="docs/") 

class Notification(models.Model):
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    payload = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)