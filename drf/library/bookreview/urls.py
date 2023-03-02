from django.urls import path

from . import views


urlpatterns = [
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorInstanceView.as_view()),
    path('book/', views.BookListView.as_view()),
]
