from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/projects/img")


# this is how you use orm
# from projects.models import Project
# Project(title="",description="",technology="",image="")
