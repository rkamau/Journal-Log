from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.
class Topic(models.Model):
    """A Topic the user is learning about"""
    topic = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        """Returns a string rep of the model"""
        return self.topic

class Entry(models.Model):
    """What was learned in a topic"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Returns a string rep of the model"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."

def get_absolute_url(self):
    return f"/topic/entries/{self.id}/"
