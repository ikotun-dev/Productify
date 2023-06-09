from django.db import models

# Create your models here.

#Employee Model <Data>
class Employee(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    employee_id = models.IntegerField(null=True)


    #String Represnetation 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#user Model
class client(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=35)

    #string representation
    def __str__(self):
        return f"{self.user_name}"

        
class task(models.Model):
    id = models.AutoField(primary_key=True)
    reminder = models.BooleanField(default=False)
    text = models.CharField(max_length=230)
    day = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.day}"

