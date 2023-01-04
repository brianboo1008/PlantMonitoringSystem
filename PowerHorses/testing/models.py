from django.db import models

# Create your models here.

class parameters(models.Model):
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	light_intensity = models.IntegerField()
	timestamp = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "parameters"
