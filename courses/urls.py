from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list_view, name='course_list'),
    path('<int:pk>/', views.course_detail_view, name='course_detail'),
]