from django.db import models

# Create your models here.

class parameters(models.Model):
	temperature = models.FloatField()
	humidity = models.FloatField()
	light_intensity = models.FloatField()
	timestamp = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "parameters"
