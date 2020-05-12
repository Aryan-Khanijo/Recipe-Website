from django.db import models

#Create your models here

class Recipes(models.Model):

    #list of category

    Categories = (
        ('North Indian','North Indian'),
        ('North-Eastern','North-Easten'),
        ('Rajasthani','Rajasthani'),
        ('Gujarati','Gujarati'),
        ('South Indian','South Indian'),
        ('Continental','Continental'),
        ('Chinese','Chinese'),
        ('Italian','Italian'),
    )

    #end list

    Title = models.CharField(
        max_length = 100,
    )
    Category = models.CharField(
        choices = Categories,
        max_length = 15,
    )
    Ingredient = models.TextField()
    
    Steps = models.TextField()
    
    Image = models.ImageField(
         default = "none.jpg"
    )

    Date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.Title

    def snippit(self):
        return self.Ingredient[:50] + '...'

    class Meta:
        verbose_name_plural = 'Recipes'
