from django.db import models


class ServiceModel(models.Model):
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=100)
    summary = models.TextField()


class LawyerModel(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    biography = models.TextField()
    education = models.CharField(max_length=100)
    attorney_certificate = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    cv = models.FileField()
    Extract = models.CharField(max_length=150, default='default')


class TVModel(models.Model):
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=100)
    video = models.CharField(max_length=500)


class CertificateModel(models.Model):
    certificate_link = models.ImageField(upload_to=f'certificates/%y/%m/%d/', default="portfolio/sample.pdf")


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()