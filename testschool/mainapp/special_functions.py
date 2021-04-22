from django.http import JsonResponse
from datetime import datetime

from mainapp.models import Student, Exam, Subject

def retJson(message):
    return JsonResponse({'message': message}, safe=False)


def handle_csv(exam, results):
    i = 1
    for each in results[1:]:
        name_index = results[0].index('Name of Student')
        dob_index = results[0].index('dob')
        datetimeobject = datetime.strptime(each[dob_index],'%m/%d/%Y')
        new_date = datetimeobject.strftime('%Y-%m-%d')
        phone_index = results[0].index('phone')
        gender_index = results[0].index('gender')
        student = Student(name=each[name_index], dob=new_date, phone=each[phone_index], exam=exam)
        student.save()
        student.save_subjects(results[0], each)
        print("Saved student - ", i)
        i += 1
        