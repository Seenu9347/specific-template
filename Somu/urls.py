from Somu.views import *
from django.urls import path
app_name='somu'
urlpatterns=[
    path('Somu/',Somu,name='Somu')
]