from rest_framework.serializers import ModelSerializer
from home.models import Instructor, Department, Article
from rest_framework import serializers
from django.contrib.auth.models import User
class DepartmentSerializer(ModelSerializer):
    class Meta :
        model = Department
        fields ="__all__"
class InstructorSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'image',
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
        read_only_fields = ['instructorID', 'user']

    def create(self, validated_data):
        instructor = Instructor(**validated_data)
        instructor.instructorID = instructor.generate_instructorID()
        instructor.save()
        return instructor

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['articleID', 'title', 'author', 'image', 'content', 'publish_date', 'upload_file']
        read_only_fields = ['articleID', 'publish_date']
    
    def create(self, validated_data):
        # Overriding the create method to ensure articleID is generated
        article = Article(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        # Ensure articleID is not updated
        validated_data.pop('articleID', None)
        return super().update(instance, validated_data)