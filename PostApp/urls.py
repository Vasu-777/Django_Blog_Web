from django.urls import path
from . import views




urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.PostListView,name='blog'),
    path('like/', views.like, name='post-like'),
    path('user/<str:username>',views.UserPostListView.as_view(),name='user-blogs'),
    path('blog-detail/<int:pk>',views.post_detail, name='blog-detail'),
    path('blog-update/<int:pk>',views.PostUpdateView.as_view(),name='blog-update'),
    path('blog-delete/<int:pk>',views.PostDeleteView.as_view(),name='blog-delete'),
    path('blog-add',views.PostCreateView.as_view(),name='blog-add'),
    path("<slug:category_slug>/",views.PostListView,name='blogs_by_category'),
   
]
