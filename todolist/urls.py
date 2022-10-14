from django.urls import path
from todolist.views import home, register, login_user, add_task_ajax
from todolist.views import logout_user, add_task, get_todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', add_task, name='add_task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_task_ajax, name='add_task_ajax'), 
]

# ASK
# /logout & /add buat apa? kan kita ga pernah akses ke add/. Atau tujuannya itu buat ngehubungin ajax di html ke fungsi views? 
# Kalo iya, Brati path itu ga selalu hubungin template (misal) add.html ke fungsi ya?