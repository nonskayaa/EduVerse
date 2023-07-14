from django import forms
from courses.models import Course
from .models import *

class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput)

class AddHomework(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ["file"]

