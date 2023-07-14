from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from courses.models import Module


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"Домашка от {self.student.username} по уроку  {self.module.title} Оценка : {self.grade}"