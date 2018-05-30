from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session

from .models import User

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

def salesregister(request):
    
    context = {}
    if 'addproperty' in request.POST:
                property = Sales propertys(region=request.POST['region']
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
                                           
                                           ,pricePerHectare=request.POST['leasepriceperhectare]
                                           
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
                                           , cgtdaterelease=request.POST['cgt_date']
                                           
                                           , BIRdst=request.POST['dst_amount']
                                           , dstdaterelease=request.POST['dst_date']
                                           
                                           , LGUtransfer=request.POST['transferfees_amount']
                                           , transferfeedaterelease=request.POST['transferfees_date']
                                           
                                           , RODlra=request.POST['lrafee_amount']
                                           , lrafeedaterelease=request.POST['lrafee_date']
                                           
                                           , RODit=request.POST['itfee_amount']
                                           , itfeedaterelease=request.POST['itfee_date']
                                           
                                           ,lbpamtrelease=request.POST['lbp_amount']
                                           , lbpdaterelease=request.POST['lbp_date']
                                           
                                           , OTHERSnotorial=request.POST['notarialfee_amount']
                                           , notorialfeedaterelease=request.POST['notarialfee_date']
                
                           )
                property.save()
                context['reg_success'] = "Account has been created."
                
    return render(request, 'register.html', context)
    return render(request, 'sales_form.html')