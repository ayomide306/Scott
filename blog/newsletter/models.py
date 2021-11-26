from django.db import models

"""
    Newsletter Model(Datanase)
"""
class Newsletter(models.Model):
    email = models.EmailField( max_length=254)
    timestamp = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.email

    #def __unicode__(self):
     #   return 
