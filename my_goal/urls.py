from django.urls import path
from . import views

app_name = 'my_goal'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
]