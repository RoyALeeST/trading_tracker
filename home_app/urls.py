from django.conf.urls import url
from home_app import views

urlpatterns = [
    url('test', views.index, name="index"),
]
