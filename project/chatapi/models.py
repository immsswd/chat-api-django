from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    text        = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        # list the data Desc
        ordering = ['-created']
        
    def __str__(self):
        return str(self.user)

