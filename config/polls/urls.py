from django.urls import path
from . import views

urlpatterns = [
    path('dbtest/', views.dbtest)
]