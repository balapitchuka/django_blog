from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.postdetail, name='post-detail'),
    path('post/<int:id>/', views.postupdate, name='post-update'),
    path('post/<int:id>/', views.postdelete, name='post-delete'),
]
