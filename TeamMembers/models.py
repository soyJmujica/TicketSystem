from django.db import models

# Create your models here.
class TeamMembers(models.Model):
	name = models.CharField(max_length=100, verbose_name="Agent's Name")
	phone = models.CharField(max_length=100, verbose_name="Phone Number")
	email = models.CharField(max_length=100, verbose_name="Email")
	offer = models.IntegerField(default=0)
	addendum = models.IntegerField(default=0)
	listing = models.IntegerField(default = 0)
	mls_attachments = models.IntegerField(default = 0)
	mls_search = models.IntegerField(default = 0)
	dotloop = models.IntegerField(default = 0)

	
	def __str__(self):
		return str(self.name)