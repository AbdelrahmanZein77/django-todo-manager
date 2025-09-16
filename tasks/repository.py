from .models import Tasks

class TaskRepository:
    
    def git_all_tasks(user):
        return Tasks.objects.filter(user=user)
    
    def create_task(user, title, description=""):
        return Tasks.objects.create(user=user, title=title, description=description)
    def delete_task(user, id):
        return Tasks.objects.filter(id=id).delete()

