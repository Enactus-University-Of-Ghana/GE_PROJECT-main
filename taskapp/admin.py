from django.contrib import admin
from . models import TaskModel,report,ProjectModel,document
# Register your models here.
"""
class TaskModelAdmin(admin.ModelAdmin):
    list_display=('task','date','isComplete')
"""
admin.site.register(TaskModel)
admin.site.register(report)
admin.site.register(ProjectModel)
admin.site.register(document)

