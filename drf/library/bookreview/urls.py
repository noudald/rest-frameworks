from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_view),
    path('author/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorInstanceView.as_view()),
    path('book/', views.BookListView.as_view()),
]
