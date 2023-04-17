from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comments/<int:comments_pk>/delete', views.comment_delete, name='comment_delete'),
    path('<int:article_pk>/likes/', views.article_like, name='article_like'),
    path('<int:article_pk>/comments/<int:comment_pk>/likes', views.comment_like, name='comment_like'),

]
