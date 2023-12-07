from django.db import models

# Create your models here.
class Company(models.Model):
    SP_ENTITY_NAME = models.CharField(max_length=200)
    SP_ENTITY_ID = models.CharField(max_length=200)
    SP_EXCHANGE_TICKER = models.CharField(max_length=200) 
    IQ_INDUSTRY_CLASSIFICATION = models.CharField(max_length=200) 
    IQ_SECTOR = models.CharField(max_length=200) 
    IQ_INDUSTRY_GROUP = models.CharField(max_length=200) 
    IQ_INDUSTRY = models.CharField(max_length=200) 
    IQ_PRIMARY_INDUSTRY = models.CharField(max_length=200) 
    SP_GEOGRAPHY = models.CharField(max_length=200) 
    SP_COUNTRY_NAME = models.CharField(max_length=200)
    
    description = models.TextField(blank=True, null=True)
    financials = models.TextField(blank=True, null=True)
    recent_news = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.SP_ENTITY_NAME
