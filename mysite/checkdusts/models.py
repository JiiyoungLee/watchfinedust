from django.db import models

class LocationInfo(models.Model):
	latitude = models.FloatField()
	longtitude = models.FloatField()
	name = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.latitude) + ", " + str(self.longtitude) + ": " + self.name

	def getLocationInfo(self):
		information = {'lat' : self.latitude, 'lng' : self.longtitude, 'name' : self.name}
		return information

class DustInfo(models.Model):
	name = models.ForeignKey(LocationInfo)
	dust = models.IntegerField()

	def __str__(self):
		return self.name.name + ": " + str(self.dust)

	def getDustInfo(self):
		information = {'name' : self.name.name, 'dust' : self.dust}
		return information



