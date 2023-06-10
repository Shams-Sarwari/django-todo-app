from django.db import models
from django.contrib.auth.models import User
import uuid


class Task(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

