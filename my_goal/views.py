from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import My_Goal
from .forms import My_GoalCreateForm 

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class My_GoalCreateView(LoginRequiredMixin,generic.CreateView):
    model = My_Goal
    template_name = 'my_goal_create.html'
    form_class = My_GoalCreateForm
    success_url = reverse_lazy('my_goal:my_goal_list')

    def form_valid(self, form):
        my_goal = form.save(commit=False)
        my_goal.user = self.request.user
        my_goal.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

# 日記編集
class My_GoalUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = My_Goal
    template_name = 'goal_update.html'
    form_class = My_GoalCreateForm

    def get_success_url(self):
        return reverse_lazy('my_goal:my_goal_detail', kwargs={'pk':self.kwargs['pk']})
    
    # 成功したとき
    def form_valid(self, form):
        messages.success(self.request,'日記を更新しました。')
        return super().form_valid(form)
    
    # 失敗したとき
    def form_invalid(self, form):
        messages.error(self.request,'日記の更新に失敗しました。')
        return super().form_invalid(form)

#　リスト
class My_GoalListView(LoginRequiredMixin,generic.ListView):
    model = My_Goal
    template_name = 'goal_list.html'
    paginate_by = 3

    def get_queryset(self):
        goals = My_Goal.objects.filter(user=self.request.user).order_by('-created_at')
        return goals