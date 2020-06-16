from django.contrib import admin
from django.urls import path
from .views import todolist, addtask,deletask

urlpatterns = [
    path('', todolist),
    path('addtask/', addtask),
    path('deletetask/<int:taskpk>/', deletask),

]