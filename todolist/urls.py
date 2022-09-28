from django.urls import path
from todolist.views import show_home, register, login_user
from todolist.views import logout_user, get_add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', get_add_task, name='get_add_task'),
]