from django.db import models

class CmdR(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text