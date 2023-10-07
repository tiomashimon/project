from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to=f'posts/%y/%m/%d/', default='posts/download.png')
    summary = models.TextField()

