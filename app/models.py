from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']