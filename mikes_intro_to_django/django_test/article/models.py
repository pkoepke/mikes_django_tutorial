from django.db import models

# Create your models here.
class Article(models.Model):
    # members of the class
    title = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published') # published date
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title
