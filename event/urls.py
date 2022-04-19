
from django.urls import path, include
from .views import index, detail, create, createevent, deleteevent

urlpatterns = [
    path('', index),
    path('detail/<id>/', detail),
    path('create/', create),
    path('createevent/', createevent),
    path('deleteevent/<id>/', deleteevent),
]