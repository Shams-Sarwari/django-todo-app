from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User
class CreateTaskForm(ModelForm):
    class Meta:
        model= Task
        fields = [
            'title', 'description', 'is_done'
        ]
