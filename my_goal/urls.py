from django.urls import path
from . import views

app_name = 'my_goal'
urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('my_goal-create/',views.My_GoalCreateView.as_view(), name="create"),
    path('my_goal-delete/',views.My_GoalDeleteView.as_view(), name="delete"),
    path('my_goal-detail/',views.My_GoaldetailView.as_view(), name="detail"),
    path('my_goal-list/',views.My_GoalListView.as_view(), name="list"),
    path('my_goal-update/<int:pk>',views.My_GoalUpdateView.as_view(), name="update"),
    

    
]