from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import csv, io, openpyxl

from mainapp.forms import FileForm
from mainapp.models import Exam, Student
from mainapp.serializers import StudentSerializer
from mainapp.special_functions import *


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def index(request):
    exams = Exam.objects.all()
    return render(request, 'index.html', {'exams': exams})


def upload_file(request):
    form = FileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            afile = request.FILES['afile']
            valid_extensions = ['csv', 'xlsx']
            afile_extension = afile.name.split(".")[-1]
            if afile_extension not in valid_extensions:
                return retJson("Not Accepted this file format")
            
            afile_text = io.TextIOWrapper(afile.file, encoding='utf-8')
            text_file = []
            if afile_extension == 'csv':
                text_file = csv.reader(afile_text, delimiter=",")
            else: 
                excel_file = openpyxl.load_workbook(afile)
                excel_file = excel_file.active
                all_rows = excel_file.rows
                for each_row in all_rows:
                    text_file.append([ cell.value for cell in each_row ])

            exam = Exam(name=form.data['name'], date=form.data['date'])
            exam.save()
            return handle_csv(exam, list(text_file))
            

    if request.method == "GET":
        return render(request, 'form.html', {'form': form})


@api_view(['POST'])
def search(request):
    if request.method == "POST":
        data = request.data
        if not 'exam__in' in data:
            return retJson("Exam not Selected")
        try:
            students = Student.objects.filter(**data)
        except:
            return Response({'error': 'post data not valid'}, status=status.HTTP_400_BAD_REQUEST)
        serialized_student = StudentSerializer(students, many=True)
        return Response(serialized_student.data, status=status.HTTP_200_OK)
