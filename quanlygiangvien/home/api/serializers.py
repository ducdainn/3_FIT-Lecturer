from rest_framework.serializers import ModelSerializer
from home.models import Instructor, Department

class DepartmentSerializer(ModelSerializer):
    class Meta :
        model = Department
        fields ="__all__"
class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'image',
            'instructorID',
            'name',
            'gender',
            'date_of_birth',
            'phone',
            'email',
            'department',
            'place_of_birth',
            'education_level',
            'job_position',
            'status'
        ]
        read_only_fields = ['instructorID' , 'user']

    def create(self, validated_data):
        instructor = Instructor(**validated_data)
        instructor.instructorID = instructor.generate_instructorID()
        instructor.save()
        return instructor