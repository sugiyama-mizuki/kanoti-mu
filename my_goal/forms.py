from .models import My_Goal

class My_GoalCreateForm(forms.ModelForm):
    class Meta:
        model=My_Goal
        fields = ('title', 'content')