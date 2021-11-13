from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article'),
    path('reporter/<str:username>/', views.reporter, name='reporter'),
]