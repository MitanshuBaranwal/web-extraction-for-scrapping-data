from django.db import models

# Create your models here.

class ExtractedText(models.Model):
    url = models.URLField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
