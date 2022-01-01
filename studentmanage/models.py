from django.db import models

# Create your models here.
class Studentmanage(models.Model):
    studentID = models.TextField(max_length=100)
    fullname = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    class Meta:
        db_table = "studentmanage"

    def __str__(self):
        return f"{self.studentID}"
