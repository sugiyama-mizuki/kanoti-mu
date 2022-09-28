from .models import Goal, My_Goal
from django import forms

class GoalCreateForm(forms.ModelForm):
    class Meta:
        model=Goal
        fields = ('title', 'content')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'