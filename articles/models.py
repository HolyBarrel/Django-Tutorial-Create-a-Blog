from django.db import models

#HELP : https://docs.djangoproject.com/en/4.1/ref/models/fields/#module-django.db.models.fields
# Create your models here.

#Model describing an article element
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #add author

    def __str__(self):
        return self.title
    
    def snippet(self): 
        return self.body[:50] + " ..."