from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.blog_detail, name='detail'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.blog_create, name='create'),
    path('update/<slug:slug>/', views.blog_update, name='update'),
    path('delete/<slug:slug>/', views.blog_delete, name='delete'),
]
