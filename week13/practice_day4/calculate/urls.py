from django.urls import path
from . import views

app_name = 'calculate'

urlpatterns = [
    path('<int:num1>/<int:num2>/', views.calculate, name="calculate"),
]
