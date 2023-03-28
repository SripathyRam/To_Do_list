from django.db import models

class todo(models.Model):
    text = models.CharField(max_length=40)
    
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Review(models.Model):
    name = models.CharField(max_length=100,null=True)
    review = models.CharField(max_length=200,null=True)

    def __str__(self):
        return "%s & %s" %(self.name,self.review)

class Contact(models.Model):
    email = models.CharField(max_length=300,null=True)
    query = models.CharField(max_length=500,null=True)

    def __str__(self):
        return "%s .............. %s" %(self.email,self.query)
