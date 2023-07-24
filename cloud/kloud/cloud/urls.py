from django.urls import path

from . import views


urlpatterns=[
        path('register/', views.Register, name='register'),
        path('', views.Login, name='login'),
        path('logout', views.Logout, name='logout'),
        path('dashboard/', views.Dashboard, name='dashboard'),
        path('add_post/', views.AddPost, name='addpost'),
        path('view_post/', views.ViewPost, name='view-post'),
        path('view-image_s/', views.Images, name='view-image_s'),
        path('view_videos/', views.Videos, name='videos'),
        path('view_docu_ment/', views.Documents, name='document')
    ]