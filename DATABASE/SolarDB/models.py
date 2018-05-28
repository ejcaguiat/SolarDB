from django.db import models
import datetime

# Create your models here.
class leaseProperty(models.Model):
    #Location Details
    region = models.CharField(max_length = 255)
    province = models.CharField(max_length = 255)
    municipality = models.CharField(max_length = 255)
    barangay = models.CharField(max_length = 255)
    #End of Location Details
    
    #Property Owner's Details
    regLandOwner = models.CharField(max_length = 255)
    contactNum = models.CharField(max_length = 255)
    Address = models.CharField(max_length = 255)
    representative = models.CharField(max_length = 255)
    #End of Property Owner's Details
    
    #Property Details
    titleNum = models.CharField(max_length = 255)
    lotNum = models.CharField(max_length = 255)
    areaHectares = models.FloatField(default = None)
    surveyNum = models.CharField(max_length=255)
    #End of Property Details
    
    #Payment Details
    pricePerHectare = models.FloatField(default = None)
    totalContractPrice = models.FloatField(default = None)
    #End of Payment Details
    
    #Released Payments
    firstPayAmount = models.FloatField(default = None)
    firstPayDate = models.DateField( default=None)
    
    secPayAmount = models.FloatField(default = None)
    secPayDate = models.DateField( default=None)
    
    thirdPayAmount = models.FloatField(default = None)
    thirdPayDate = models.DateField(default=None)
    
    fourthPayAmount = models.FloatField(default = None)
    fourthPayDate = models.DateField( default=None)
    
    fifthPayAmount = models.FloatField(default = None)
    fifthPayDate = models.DateField( default=None)
    
    sixthPayAmount = models.FloatField(default = None)
    sixthPayDate = models.DateField( default=None)
    
    seventhPayAmount = models.FloatField(default = None)
    seventhPayDate = models.DateField(default=None)
    
    eigthPayAmount = models.FloatField(default = None)
    eigthPayDate = models.DateField(default=None)
    
    ninthPayAmount = models.FloatField(default = None)
    ninthPayDate = models.DateField(default=None)
    
    tenthPayAmount = models.FloatField(default = None)
    tenthPayDate = models.DateField(default=None)
    #End of Released Payments
    
    releasedPayment = models.FloatField(default = None)
    
    
    Payee = models.CharField(max_length = 255)
    area = models.FloatField(default = None)