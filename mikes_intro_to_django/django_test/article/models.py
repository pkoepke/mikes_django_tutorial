from django.db import models

# Create your models here.
# django.db.models.Model is a class that all Django models should inherit from (I think). It manages how your models interact with the database when storing or retrieving data.
class Article(models.Model):
    # members of the class
    title = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published') # published date
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title
