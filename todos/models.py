from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=True)

    def __str__(self):
        created = self.created.strftime("%Y-%m-%d %H:%M:%S")
        print(created)
        return f"{self.id} ({created}) {self.title}"
