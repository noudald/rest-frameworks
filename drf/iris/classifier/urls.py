from django.urls import path

from . import views


urlpatterns = [
    path('classifier/input/', views.IrisInputList.as_view()),
    path('classifier/input/<int:pk>/', views.IrisInputDetail.as_view()),
    path('classifier/output/', views.IrisOutputList.as_view()),
    path('classifier/output/<int:pk>/', views.IrisOutputDetail.as_view()),
]

