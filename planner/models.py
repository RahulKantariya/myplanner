from django.db import models

# Create your models here.
class Profile(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Weight=models.FloatField()
    Height=models.FloatField()
    Gender=models.CharField(max_length=10)
    StartingDate=models.DateField()
    EndingDate=models.DateField()
    DueToDietFor=models.TextField(blank=True)
    Carbohydrates=models.FloatField()
    Fats=models.FloatField()
    Protin=models.FloatField()
    AfterWakeUp=models.TextField(blank=True)
    BeforeBreakfast=models.TextField(blank=True)
    Breakfast=models.TextField(blank=True)
    Lunch=models.TextField(blank=True)
    Snacks=models.TextField(blank=True)
    Dinner=models.TextField(blank=True)
    MidNeightDrink=models.TextField(blank=True)
    Notes=models.TextField(blank=True)
    Excercise=models.TextField(blank=True)



    def __str__(self):
        return  self.Name