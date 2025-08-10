from django.urls import path 
from . import views



urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members , name="members"),
    path("members/detail/<int:id>", views.detail, name="member_detail")
]
