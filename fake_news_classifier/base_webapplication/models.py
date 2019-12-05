from django.db import models
from django.utils import timezone

# Create your models here.
class TimeStampedModel(models.Model):
	 created_on = models.DateTimeField(auto_now_add=True)

	 class Meta:
		 abstract = True

class TweetURL(TimeStampedModel):
	TweetUrl = models.CharField(max_length=300)

	def __str__(self):
		return self.TweetUrl

