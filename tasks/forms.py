from django.forms import ModelForm
from .models import Task

class CreateTaskForm(ModelForm):
    class Meta:
        model= Task
        fields = [
            'title', 'description', 'is_done'
        ]