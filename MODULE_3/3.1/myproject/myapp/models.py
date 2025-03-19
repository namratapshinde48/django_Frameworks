from django.db import models  

class Drinks(models.Model):  
    drink_name = models.CharField(max_length=200)  # Updated from 'drink' to 'drink_name'
    price = models.IntegerField()  

    def __str__(self):  
        return self.drink_name  
