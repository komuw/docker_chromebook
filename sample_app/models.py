from django.db import models

# Create your models here


class Book(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'name:%s' %(self.name)

