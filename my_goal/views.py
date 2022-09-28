from django.views import generic
from .forms import GoalCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Goal
from .forms import  GoalCreateForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

