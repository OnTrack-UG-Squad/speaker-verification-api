from django.db import models

# Create your models here.

class speaker_verification_user(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # Allow users to be created without a MFCC, will populate after processing of data.
    mfcc = models.BinaryField(blank=True, null=True)
