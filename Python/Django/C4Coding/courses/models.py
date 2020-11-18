from django.db import models

# Create your models here.

class Courses(models.Model):
    instructor = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    courseUrl = models.URLField(default="www.google.com")

    def __str__(self):
        return self.title