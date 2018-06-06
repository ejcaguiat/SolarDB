from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session

from .models import User
from .models import salesProperty
from .models import leaseProperty

# Create your views here.
def index(request):
    

    context = {}
    if request.method == "POST":
        if 'login' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

                request.session['user'] = user.pk
                #request.session['type'] = user.get_type()
                return HttpResponseRedirect('homepage')

            except User.DoesNotExist:
                context['log_error'] = 'Cannot find an account with that combination.'
                
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
            return render(request, 'register.html', context)
                
    return render(request, 'login.html', context)


def register(request):
    context = {}
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
    return render(request, 'register.html', context)

def homepage(request):
    try:
        loggeduser = User.objects.get(id=request.session['user'])
    except(KeyError, User.DoesNotExist):
        loggeduser = 0
    context = {
            'loggeduser':loggeduser,
    }
    return render(request, 'homepage.html', context)

def salesview(request):
    all_properties =salesProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }

    
    return render(request, 'displaysales.html',context)

def leaseview(request):
    all_properties =leaseProperty.objects.all()
    context = {
            'all_properties':all_properties,
    }

    
    return render(request, 'displaylease.html',context)

def leaseregister(request):

    return render(request, 'lease_form.html')

def salesregister(request):
    
    context = {}
    if 'addproperty' in request.POST:
                property =salesProperty(region=request.POST['region']
                                            , province=request.POST['province']
                                           
                                            , municipality=request.POST['municipality']
                                            , barangay=request.POST['barangay']
                                           
                                            ,regLandOwner=request.POST['registeredlandowner']
                                            , representative=request.POST['representative']
                                           
                                           , Address=request.POST['address']
                                           , contactNum=request.POST['contactnumber']
                                           
                                           , titleNum=request.POST['titlenumber']
                                           , lotNum=request.POST['lotnumber']
                                           
                                           , areaHectares=request.POST['size']
                                           , surveyNum=request.POST['surveynumber']
                                           
                                           ,pricePerHectare=request.POST['leasepriceperhectare']
                                           
                                           , firstPayAmount=request.POST['1stpayment_amount']
                                           , firstPayDate=request.POST['1stpayment_date']
                                           
                                           , secPayAmount=request.POST['2ndpayment_amount']
                                           , secPayDate=request.POST['2ndpayment_date']
                                           
                                           , thirdPayAmount=request.POST['3rdpayment_amount']
                                           , thirdPayDate=request.POST['3rdpayment_date']
                                           
                                           , fourthPayAmount=request.POST['4thpayment_amount']
                                           , fourthPayDate=request.POST['4thpayment_date']
                                           
                                           
                                           , fifthPayAmount=request.POST['5thpayment_amount']
                                           , fifthPayDate=request.POST['5thpayment_date']
                                           
                                           , sixthPayAmount=request.POST['6thpayment_amount']
                                           , sixthPayDate=request.POST['6thpayment_date']
                                           
                                           , seventhPayAmount=request.POST['7thpayment_amount']
                                           , seventhPayDate=request.POST['7thpayment_date']
                                           
                                           , eigthPayAmount=request.POST['8thpayment_amount']
                                           , eigthPayDate=request.POST['8thpayment_date']
                                           
                                           , ninthPayAmount=request.POST['9thpayment_amount']
                                           , ninthPayDate=request.POST['9thpayment_date']
                                           
                                           , tenthPayAmount=request.POST['10thpayment_amount']
                                           , tenthPayDate=request.POST['10thpayment_date']
                                           
                                           , BIRcgt=request.POST['cgt_amount']
                                           
                                           
                                           , BIRdst=request.POST['dst_amount']
                                           
                                           
                                           , LGUtransfer=request.POST['transferfees_amount']
                                           
                                           
                                           , RODlra=request.POST['lrafee_amount']
                                           
                                           
                                           , RODit=request.POST['itfee_amount']
                                            , OTHERSnotorial=request.POST['notarialfee_amount']
                                           ,totalContractPrice= 0000
                                            , releasedPayment =0000
                                        , balance =0000
                                        , SUMother =0000
                                        , TAXother =0000
                                        , area =0000
                                           
                                           
                
                           )
                property.save()
                return render(request, 'sales_form.html')
       
    return render(request, 'sales_form.html')


