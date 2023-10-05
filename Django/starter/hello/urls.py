from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.index, name="index"),
    path("ale", views.ale, name="ale"),
    path("caro", views.caro, name="caro"),
    path("<str:name>", views.greet, name="greet")
]