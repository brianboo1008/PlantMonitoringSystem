from django.db import models

# Create your models here.

class parameters(models.Model):
    nodeID = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    light_intensity = models.FloatField()
    raindrop = models.IntegerField(default=1024)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "parameters"

class nodeDetails(models.Model):
    #parameter = models.ForeignKey(parameters, on_delete=models.CASCADE)
    nodeID = models.CharField(max_length=255)
    nodePIC = models.CharField(max_length=255)
    nodePICContact = models.CharField(max_length=255)
    nodeLastMaintenance = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "nodeDetails"