from django.urls import path
from . import views

app_name = 'number_print'

urlpatterns = [
    path('<int:num>', views.number_print, name="number_print"),
]
