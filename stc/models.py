from django.db import models

# Create your models here.
class Stc(models.Model):

    classID = models.TextField(max_length=100)
    classname = models.CharField(max_length=100)

    class Meta:
        db_table = "stc"

    def __str__(sus):
        return f"{sus.classID}" f": {sus.classname}"
