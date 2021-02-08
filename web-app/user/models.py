from django.db import models
from django.contrib.auth.models import User


class driver(models.Model):#继承model类
    CARTYPE_CHOICES = [("economy", "economy"),("business", "business"), ("luxury", "luxury"), ("presidential", "presidential")]
    CAPA_CHOICES = [(2, 2), (5, 5), (7, 7)]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isDriver = models.BooleanField(default=False) 
    carType = models.CharField(max_length=999,default = 'None', choices = CARTYPE_CHOICES)
    plateNum = models.CharField(max_length=999,default = 'None')
    capa = models.IntegerField(default=0, choices = CAPA_CHOICES)
    def _str_(self):
      return f'the car belongs to {self.user.username}'
            
#    def create_driver(sender, **kwargs):
#      if kwargs['created']:
#        driver = driver.objects.create(user=kwargs['instance'])
    def save(self):
      super().save()

      
class ride(models.Model):#继承model类
    PNUM_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]
    AREA_CHOICES = [("N", "North"), ("S", "South"), ("E", "East"), ("W", "West"), ("C", "Central Area")]
    user = models.ManyToManyField(User)    
    destination = models.CharField(max_length=999,default = 'None')#useless field  #form owner
    shareable = models.BooleanField(default=False)                                  #form owner
    area = models.CharField(max_length=999, default = 'None',choices = AREA_CHOICES) #form owner
    startTime  = models.DateTimeField()                                               #form owner
    passengerNum = models.IntegerField(choices = PNUM_CHOICES)#发起者                 #form owner
    driverId = models.IntegerField(default = '0')                                   #form driver
    ownerId = models.IntegerField(default = '0')                                    #form owner
    confirmed = models.BooleanField(default=False)                                  #form driver
    completed = models.BooleanField(default=False)
    driverName = models.CharField(max_length=999, default = 'None')
    carType = models.CharField(max_length=999,default = 'None')
    plateNum = models.CharField(max_length=999,default = 'None')
    def _str_(self):
      return f'the car {self.carType} belongs to {self.user.username}'
