from django.db import models

class Poster(models.Model):
#    title = models.TextField()
    file = models.FileField()
    def __str__(self):
        return self.title
