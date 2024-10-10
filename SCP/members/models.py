from django.db import models


class member(models.Model):
    # member is a DB table
    # primary key is auto id...
    firstname = models.TextField() # column
    lastname = models.TextField()
    emailaddess = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
