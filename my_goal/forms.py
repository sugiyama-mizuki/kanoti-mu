from .models import My_Goal
from django import forms

class My_GoalCreateForm(forms.ModelForm):
    class Meta:
        model=My_Goal
        fields = ('title', 'content')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'