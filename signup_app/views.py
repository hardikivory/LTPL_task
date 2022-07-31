import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests import session

from order_project.settings import EMAIL_HOST_USER
from .models import User
from .forms import UserCreateForm
from .helper import otp_gen, send_email

def UserSignUpView(request):
    '''
    This Function Through User Create own Account.
    '''
    if request.method == 'POST':
        fm = UserCreateForm(request.POST)
        if fm.is_valid():
            fm.save()
            print('Registation Successfully...')
            return redirect('signin')
        else:
            print('Registation Failed...')
    fm = UserCreateForm()
    return render(request, 'signup.html',{'form': fm})


def UserSignInView(request):
    '''
    This Function request email and check email is valid or not
    and send OTP on email.
    '''

    if request.method == 'POST':
        email = request.POST['email']    
        try:
            check_user = User.objects.get(email = email)

            if check_user is not None:
                otp = otp_gen()

                subject = 'OTP Authentication'
                message = f'''\n
                    Signin OTP: \n
                    {otp}
                '''
                email = email.lower()
                from_email = EMAIL_HOST_USER  
                to_email =  email
                
                data = {
                    'subject': subject,
                    'message': message,
                    'from_email': from_email,
                    'to_email': to_email,
                }
                send_email(data= data)

                request.session['otp'] = otp 
                return redirect('otp')          
        except:
            print('Email Id not matched...')
    return render(request, 'signin.html')




def OtpView(request):
    '''
    This Function request OTP and check if OTP
    is match or not.
    '''
    if request.method == 'POST':
        otp1 = request.POST['otp1']
        if otp1 == request.session.get('otp'):
            print('Login Successfully..')
            request.session.flush()
            return render(request,'home.html')
        else:
            print('Sign in Failed...')
            

    
    return render(request, 'otp.html')