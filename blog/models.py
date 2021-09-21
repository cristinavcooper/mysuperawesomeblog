from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_lenght=300)
	date = models.DateTimeField()
	text = models.CharField()
	image = models.ImageField(upload_to='event_images/') 