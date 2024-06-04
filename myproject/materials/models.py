from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='materials/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(User)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.material:
            return f'Comment by {self.author} on {self.material}'
        else:
            return f'Comment by {self.author} on {self.project}'
