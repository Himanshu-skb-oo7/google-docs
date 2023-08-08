import uuid

from django.db import models

# Create your models here.
class Doc(models.Model):
    id = models.UUIDField(max_length=32, default=uuid.uuid4, primary_key=True)
    content = models.TextField()
    