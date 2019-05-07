# from django.contrib import admin
from django.urls import path, include
# import todo_list.urls
from .import views

app_name = 'todo_list'
urlpatterns = [
    # path('', admin.site.urls),
    path('index/', views.index, name='主页'),
    path('inform/', views.inform, name='介绍页面'),
    path('edit/<forloop_counter>', views.edit, name='编辑页面'),
    path('delete/<forloop_counter>', views.delete, name='删除页面'),
    path('status/<forloop_counter>', views.status, name='完成与否'),
]

 