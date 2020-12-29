from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='frontend.blog.index'),
    path('addpost/', views.addpost, name="frontend.blog.addpost"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
