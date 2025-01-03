from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    age_limited  = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

'''
Buyer.objects.create(name= 'Serge', balance = 1500.05, age = 22)
Buyer.objects.create(name= 'Rosaria', balance = 42.15, age = 62)
Buyer.objects.create(name= 'Rasor', balance = 0.5, age = 12)

Game.objects.create(title= 'Atomic Heart', cost= 31, size= 46.2, 
    description='The alternative reality of the 1950s', age_limited=1)
Game.objects.create(title= 'Farmington', cost= 10, size=0.5, 
    description='You are a farmer', age_limited=0)
Game.objects.create(title= 'Subnautica', cost= 15, size= 36, 
    description='Underwater world', age_limited=1)

Game.objects.get(id=1).buyer.set((1,2)) 
Game.objects.get(id=2).buyer.set((2,3)) 
Game.objects.get(id=3).buyer.set((1,2)) 

'''