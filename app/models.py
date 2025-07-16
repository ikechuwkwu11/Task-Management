from django.db import models
from datetime import datetime

class User(models.Model):
    Roles_Choices = ('admin','Admin'),('manager','Project Manager'),('employee','Employee')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=Roles_Choices, default='employee')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()


    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,default='pending')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.project.name}'


class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'commented by {self.author.username} on {self.task.title}'

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='audit_log')
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,related_name='audit_log')

    def __str__(self):
        return f'{self.user} - {self.action} @ {self.timestamp}'