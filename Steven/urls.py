from Steven.views import *
from django.urls import path
app_name='Steven'
urlpatterns=[
    path('Steven/',Steven,name='Steven')
]