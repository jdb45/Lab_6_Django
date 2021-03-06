from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date = models.CharField(max_length=25)
    notes = models.TextField()

    def __str__(self):
        return '%s visted? %s' % (self.name, self.visited, self.date, self.notes)
