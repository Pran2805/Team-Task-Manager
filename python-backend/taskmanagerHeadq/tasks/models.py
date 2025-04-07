from django.db import models

# Create your models here.
class task(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=100, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    status = models.CharField(max_length=100, choices=[('Started', 'Started'), ('pending', 'Pending'), ('in progress', 'In Progress'), ('completed', 'completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groupid = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title

class subtask(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=[('Started', 'Started'), ('pending', 'Pending'), ('in progress', 'In Progress'), ('completed', 'completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

   
    task = models.ForeignKey(task, on_delete=models.CASCADE, related_name='subtasks')
    def __str__(self):
        return self.name