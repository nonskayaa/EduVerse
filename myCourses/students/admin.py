from django.contrib import admin

from .models import AssignmentSubmission

# @admin.register(AssignmentSubmission)
# class AssignmentSubmissionAdmin(admin.ModelAdmin):
#     list_display = ['file','grade']

admin.site.register(AssignmentSubmission)

