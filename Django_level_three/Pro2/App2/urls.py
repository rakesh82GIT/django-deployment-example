from django.conf.urls import url, include
from App2 import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
    ]
