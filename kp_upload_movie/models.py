from django.db import models
from django.utils import timezone

# Create your models here.
def user_path(instance, filename):
    return '%s/%s' % (instance.username, filename)

class Movie(models.Model):
    username = models.CharField(max_length = 100)
    update_time = models.DateTimeField(auto_now_add=True)
    movie = models.FileField(upload_to = user_path)

    def generate(self):
        self.update_time = timezone.now()
        self.save()

    def __str__(self):
        return self.username
