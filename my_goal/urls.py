from django.urls import path
from . import views

app_name = 'my_goal'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('create/',views.CreateView.as_view(), name="create"),
    path('delete/',views.DeleteView.as_view(), name="delete"),
    path('detail/',views.DetailView.as_view(), name="detail"),
    path('list/',views.ListView.as_view(), name="list"),
    path('update/',views.UpdateView.as_view(), name="update"),

]