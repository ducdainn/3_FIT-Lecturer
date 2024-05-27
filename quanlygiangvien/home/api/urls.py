
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, InstructorViewSet, ArticleViewSet, UserListView, APIRoot
from .views import UserListView
from django.urls import path

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'article', ArticleViewSet)
# Thêm URL pattern cho class-based view
urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),  # URL gốc của API 
    path('users', UserListView.as_view(), name='user-list'),
]
urlpatterns += router.urls