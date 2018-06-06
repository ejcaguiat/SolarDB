from django.db import models
import datetime

# Create your models here.
class salesProperty(models.Model):
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
    
    secPayAmount = models.FloatField(default = 0)
    secPayDate = models.DateField( default=None)
    
    thirdPayAmount = models.FloatField(default = 0)
    thirdPayDate = models.DateField(default=None)
    
    fourthPayAmount = models.FloatField(default = 0)
    fourthPayDate = models.DateField( default=None)
    
    fifthPayAmount = models.FloatField(default = 0)
    fifthPayDate = models.DateField( default=None)
    
    sixthPayAmount = models.FloatField(default = 0)
    sixthPayDate = models.DateField( default=None)
    
    seventhPayAmount = models.FloatField(default = 0)
    seventhPayDate = models.DateField(default=None)
    
    eigthPayAmount = models.FloatField(default = 0)
    eigthPayDate = models.DateField(default=None)
    
    ninthPayAmount = models.FloatField(default = 0)
    ninthPayDate = models.DateField(default=None)
    
    tenthPayAmount = models.FloatField(default = 0)
    tenthPayDate = models.DateField(default=None)
    
    releasedPayment = models.FloatField(default=None)
    balance = models.FloatField(default=None)
    #End of Released Payments
    
    #Taxes and Registration Fees
    BIRcgt = models.FloatField(default=None)
    BIRdst = models.FloatField(default=None)
    LGUtransfer = models.FloatField(default=None)
    RODlra = models.FloatField(default=None)
    RODit = models.FloatField(default=None)
    OTHERSnotorial = models.FloatField(default=None)
    SUMother = models.FloatField(default=None)
    #missing LBP column
    TAXother = models.FloatField(default=None)
    #End of Taxes and Registration Fees
    
    
    Payee = models.CharField(max_length = 255)
    area = models.FloatField(default = None)
    
    
    
    
class leaseProperty(models.Model):
    #missing title number, lot no, advance payment (lease price per year, amount, date release), years 1-30, balance
    
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
    
     #Payment Details
    pricePerHectare = models.FloatField(default = None)
    totalContractPrice = models.FloatField(default = None)
    #End of Payment Details
    
    #Released Payments

    
    
    
    #Taxes and Registration Fees
    BIRcgt = models.FloatField(default=None)
    BIRdst = models.FloatField(default=None)
    LGUtransfer = models.FloatField(default=None)
    RODlra = models.FloatField(default=None)
    RODit = models.FloatField(default=None)
    OTHERSnotorial = models.FloatField(default=None)
    SUMother = models.FloatField(default=None)
    TAXother = models.FloatField(default=None)
    #End of Taxes and Registration Fees
    
    Payee = models.CharField(max_length = 255)
    area = models.FloatField(default = None)
    taxDec = models.CharField(max_length=255)
    dateRelease = models.DateField(default=None)
    
    
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    choices = ((0, 'Regular User'), (1, 'Admin'))
    accountType = models.IntegerField(choices=choices, default = 0)
    
    
    