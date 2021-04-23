from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



class Exam(models.Model):
    name = models.CharField(max_length=255, blank=False)
    date = models.DateField()

    def __str__(self):
        return self.name + " - " + str(self.date)


class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='students')
    subjects = models.JSONField()

    def __str__(self):
        return self.name

    # def save_subjects(self, columns, student):
    #     for each in columns:
    #         if each in VALID_SUBJECTS:
    #             subject = Subject(name=each, score=student[columns.index(each)], student=self)
    #             subject.save()


# class Subject(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')

#     def __str__(self):
#         return self.name