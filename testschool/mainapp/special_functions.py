from django.http import JsonResponse
from datetime import datetime

from mainapp.models import Student, Exam


VALID_SUBJECTS = ['Maths', 'English', 'Nepali', 'Social', 'Science', 'Optional Maths', 'Account']

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
        subjects = {}
        for each_col in results[0]:
            if each_col in VALID_SUBJECTS:
                sub_index = results[0].index(each_col)
                subjects[each_col] = each[sub_index]

        student = Student(name=each[name_index], dob=new_date, phone=each[phone_index], exam=exam, subjects=subjects)
        student.save()
        i += 1
        