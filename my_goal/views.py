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

class GoalCreateView(LoginRequiredMixin,generic.CreateView):
    model = Goal
    template_name = 'goal_create.html'
    form_class = GoalCreateForm
    success_url = reverse_lazy('my_goal:goal_list')

    def form_valid(self, form):
        my_goal = form.save(commit=False)
        my_goal.user = self.request.user
        my_goal.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)