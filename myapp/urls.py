from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('updatetasks/<str:pk>/',views.updatetodo,name="updatetasks"),
    path('delete/<str:pk>/',views.removetask,name="delete"),
]