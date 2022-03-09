from django.db import models

# Create your models here.

class Todo(models.Model):
    """
    Data for a todo-list
    """

    name = models.CharField(max_length=128, blank=True)
    content = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name
