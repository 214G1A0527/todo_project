from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=255)
    due_datetime = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    creator = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
