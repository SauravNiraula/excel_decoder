from rest_framework import serializers

from mainapp.models import Student, Exam


# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ['id', 'name', 'score']


class StudentSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'dob', 'phone', 'subjects']


class ExamSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = Exam
        fields = ['id', 'name', 'date', 'students']