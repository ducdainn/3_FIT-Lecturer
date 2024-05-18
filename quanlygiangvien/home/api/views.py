from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer, InstructorSerializer
from home.models import Instructor, Department

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer