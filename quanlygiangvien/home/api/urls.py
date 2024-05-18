
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, InstructorViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'instructors', InstructorViewSet)

urlpatterns = router.urls