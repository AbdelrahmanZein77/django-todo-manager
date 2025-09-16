from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.Login, name= 'login'),
    path('logout/', views.logout_views, name='logout'),
    path('home/', views.home, name='home'),
    path('tasks/', views.all_tasks, name='tasks'),
    path('update/<int:task_id>/', views.UpdateTask, name='update_task'),
    path('toggle/<int:task_id>/', views.Toggle_task, name='Toggle_task'),
    path('delete/<int:task_id>/', views.delelte_task, name='delelte_task'),
    path('tasks_api/', views.Tasks_api, name='tasks_api'),
    path('tasks_api_pk/<int:pk>/', views.Tasks_api_pk, name='tasks_api_pk'),
    path('api/token/', obtain_auth_token, name='api_token'),
]