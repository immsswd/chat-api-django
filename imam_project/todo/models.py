from django.db import models

# Create your models here.
class Todo(models.Model):
    title       = models.CharField(max_length=20)
    body        = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
    