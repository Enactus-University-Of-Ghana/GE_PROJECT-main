
from .models import ProjectModel
from .models import TaskModel
#task_data=TaskModel.objects.filter(id).values()
#project_data=ProjectModel.objects.all().values()

def calc_budget():
    for t in task_data:
        budget=TaskModel.budget+budget
    ProjectModel.budget=budget
    return budget