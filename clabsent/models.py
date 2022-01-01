from django.db import models
from django.db.models.fields import AutoField

from studentmanage.models import Studentmanage
from stc.models import Stc

# Create your models here.
class Clabsent(models.Model):
    studentID = models.ForeignKey(Studentmanage, on_delete=models.CASCADE)
    classname = models.ForeignKey(Stc, on_delete=models.CASCADE)
    dateabsent = models.DateField()

    class Meta:
        db_table = "clabsent"

    def __str__(self):
        return f"{self.studentID} {self.classname} ({self.dateabsent})"
