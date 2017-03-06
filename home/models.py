from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Mate(models.Model):
    first_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250, blank=True)
    picture = models.CharField(max_length=500, blank=True)
    title= models.CharField(max_length=250, blank=True)
    description= models.TextField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Nickname(models.Model):
    mate= models.ForeignKey(Mate,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
