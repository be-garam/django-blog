from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('about.html', views.AboutView.as_view(), name='about'),
    path('contact.html', views.ContactView.as_view(), name='contact'),
]
