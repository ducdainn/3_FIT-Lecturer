from django.contrib import admin
from django.urls import path, include
from .views import HomeClass, LoginClass, InstructorManagement,InstructorDetailView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('login/', LoginClass.as_view(), name='login'),
    path('home/', HomeClass.as_view(), name='home'),    
    path('administrator/', InstructorManagement.as_view(), name='administrator'),
    path('instructor/<str:instructor_id>/', InstructorDetailView.as_view(), name='instructor'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)