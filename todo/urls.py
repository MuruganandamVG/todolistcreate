from django.urls import path
from .views import index,delete

urlpatterns=[
    path('',index,name='index'),
    path('delete/<str:pk>',delete,name='delete')
]