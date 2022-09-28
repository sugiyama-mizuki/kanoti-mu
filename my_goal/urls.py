from django.urls import path
from . import views

app_name = 'my_goal'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('my_goal/',views.My_GoalCreateView.as_view(),name="my_goal_create"),
]