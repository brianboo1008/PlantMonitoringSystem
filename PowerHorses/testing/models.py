from django.db import models

# Create your models here.

class parameters(models.Model):
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	light_intensity = models.IntegerField()
	
	class Meta:
		db_table = "parameters"
