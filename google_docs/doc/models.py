import uuid

from django.db import models
from users import models as user_models

class DocQuerySet(models.QuerySet):
    def visible_to_user(self, user):
        return self.filter(models.Q(owner=user) | models.Q(shared_with=user)).distinct()

# Create your models here.
class Doc(models.Model):
    id = models.UUIDField(max_length=32, default=uuid.uuid4, primary_key=True)
    content = models.TextField(null=True)
    title = models.CharField(max_length=120, null=False)
    owner = models.ForeignKey(user_models.CustomUser, on_delete=models.CASCADE, null=True)
    shared_with = models.ManyToManyField(user_models.CustomUser, related_name='shared_docs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DocQuerySet.as_manager() 

    def __str__(self):
        return self.title
    