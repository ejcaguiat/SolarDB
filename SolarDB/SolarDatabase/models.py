from django.db import models
import datetime

# Create your models here.
class leaseProperty(models.Model):
    #Location Details
    region = models.Charfield(max_length = 255)
    province = models.Charfield(max_length = 255)
    municipality = models.Charfield(max_length = 255)
    barangay = models.Charfield(max_length = 255)
    #End of Location Details
    
    #Property Owner's Details
    regLandOwner = models.Charfield(max_length = 255)
    contactNum = models.Charfield(max_length = 255)
    Address = models.Charfield(max_length = 255)
    representative = models.Charfield(max_length = 255)
    #End of Property Owner's Details
    
    #Property Details
    titleNum = models.Charfield(max_length = 255)
    lotNum = models.Charfield(max_length = 255)
    areaHectares = models.Floatfield(default = None)
    surveyNum
    #End of Property Details
    
    #Payment Details
    pricePerHectare = models.Floatfield(default = None)
    totalContractPrice = models.Floatfield(default = None)
    #End of Payment Details
    
    #Released Payments
    firstPayAmount = models.Floatfield(default = None)
    firstPayDate = models.DateField(_("Date"), default=None)
    
    secPayAmount = models.Floatfield(default = None)
    secPayDate = models.DateField(_("Date"), default=None)
    
    thirdPayAmount = models.Floatfield(default = None)
    thirdPayDate = models.DateField(_("Date"), default=None)
    
    fourthPayAmount = models.Floatfield(default = None)
    fourthPayDate = models.DateField(_("Date"), default=None)
    
    fifthPayAmount = models.Floatfield(default = None)
    fifthPayDate = models.DateField(_("Date"), default=None)
    
    sixthPayAmount = models.Floatfield(default = None)
    sixthPayDate = models.DateField(_("Date"), default=None)
    
    seventhPayAmount = models.Floatfield(default = None)
    seventhPayDate = models.DateField(_("Date"), default=None)
    
    eigthPayAmount = models.Floatfield(default = None)
    eigthPayDate = models.DateField(_("Date"), default=None)
    
    ninthPayAmount = models.Floatfield(default = None)
    ninthPayDate = models.DateField(_("Date"), default=None)
    
    tenthPayAmount = models.Floatfield(default = None)
    tenthPayDate = models.DateField(_("Date"), default=None)
    #End of Released Payments
    
    releasedPayment = models.Floatfield(default = None)
    
    
    Payee = models.Charfield(max_length = 255)
    area = models.Floatfield(default = None)