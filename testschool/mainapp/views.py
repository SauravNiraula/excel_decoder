from django.shortcuts import render
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
import csv, io

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
            text_file = None
            if afile_extension == 'csv':
                text_file = csv.reader(afile_text, delimiter=",")
            # else: 
                # excel_file = xlrd.open_workbook(

            exam = Exam(name=form.data['name'], date=form.data['date'])
            exam.save()
            handle_csv(exam, list(text_file))
            

            return retJson("Data and File Accepted")
        return retJson("Not Accepted")

    if request.method == "GET":
        return render(request, 'form.html', {'form': form})


@csrf_exempt
def search(request):
    if request.method == "POST":
        data = request.POST
        if not data['exam']:
            return retJson("Exam not Selected")