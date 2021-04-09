from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

class Upload_file(models.Model):
    title = models.TextField()
    audio = models.FileField(upload_to='audio/')
    
    def __str__(self):
        return self.title
