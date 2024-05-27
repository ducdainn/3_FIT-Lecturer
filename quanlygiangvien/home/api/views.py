from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer, InstructorSerializer, ArticleSerializer
from home.models import Instructor, Department , Article
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.reverse import reverse

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
class UserListView(APIView):
    def get(self, request):
        # Lấy danh sách user không phải là staff
        users = User.objects.filter(is_staff=False)
        
        # Tạo list chứa thông tin của từng user
        user_list = [{'username': user.username, 'is_staff': user.is_staff} for user in users]
        
        # Trả về response
        return Response(user_list, status=status.HTTP_200_OK)
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'departments': reverse('department-list', request=request, format=format),
            'instructors': reverse('instructor-list', request=request, format=format),
            'articles': reverse('article-list', request=request, format=format),
            'users': reverse('user-list', request=request, format=format),
        })