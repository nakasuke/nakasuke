from django.db import models

# Create your models here.

#会社情報を格納するテーブル
class Company(models.Model):
    name      = models.CharField(max_length=256)
    industory = models.CharField(max_length=256)
    location  = models.CharField(max_length=256)

    def __str__(self):
        return self.name

#会社に紐づく従業員情報を格納するテーブル
class Employee(models.Model):
    name    = models.CharField(max_length=256)
    age     = models.PositiveIntegerField()
    company = models.ForeignKey(Company,related_name='Employees',on_delete=models.CASCADE)

    def __str__(self):
        return self.name