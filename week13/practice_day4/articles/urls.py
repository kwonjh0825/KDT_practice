from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('catch/', views.catch, name="catch"),
    path('throw/', views.throw, name="throw"),
]
