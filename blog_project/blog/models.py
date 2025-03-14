from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # thêm trường image
    image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    # thêm trường link
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']