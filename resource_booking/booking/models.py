from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Room(models.Model):
    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room} - {self.start_time} - {self.end_time}"