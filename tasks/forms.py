from django import forms
from .models import Homework


class HomeworkForm(forms.ModelForm):

    class Meta:
        model = Homework
        fields = '__all__'

        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }