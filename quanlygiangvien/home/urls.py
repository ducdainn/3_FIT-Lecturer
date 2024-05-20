from django.contrib import admin
from django.urls import path, include
from .views import HomeClass, LoginClass, InstructorManagement,InstructorDetailView, ArticlePost, ArticleDetailView, ForumDetailView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('login/', LoginClass.as_view(), name='login'),
    path('home/', HomeClass.as_view(), name='home'),    
    path('instmanage/', InstructorManagement.as_view(), name='instmanage'),
    path('instructor/<str:instructor_id>/', InstructorDetailView.as_view(), name='instructor'),
    path('articlepost/', ArticlePost.as_view(), name='articlepost'),
    path('article/<str:instructor_id>/', ArticleDetailView.as_view(), name='article'),
    path('forum/', ForumDetailView.as_view(), name='forum'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        