from django.db import models
from django.utils import timezone
 
 
class memo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
 
    def _str_(self):
        return self.title


