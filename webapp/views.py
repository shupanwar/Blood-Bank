from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.db.utils import IntegrityError
from . models import Donor

# for sending mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint


def generateOTP(n): 
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def sendmail(email,name,otp):
    try:
        message = """<html>
                <body>
                    <h1 style='color:red'>Blood Bank Login OTP</h1> <hr>
                    Hello {0},<br><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        Your login otp is <b> {1}  </b>, please don't share to anyone.
                            <br>
                        <br><b> Thanks
                        <br><br>    Blood Bank
                        <br>    Indore Branch </b>
                </body></html>""".format(name,otp)
        smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
        smtp.starttls()
        smtp.login("justsample4mail@gmail.com","sample@123")
        msg = MIMEMultipart() 
        msg['From'] ="justsample4mail@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Blood Bank Login OTP"
        msg.attach(MIMEText(message, 'html'))
        smtp.send_message(msg)
        smtp.quit()
        print("Mail Send Successfully ! ")        
        return True
    except Exception as ex:
        print("Mail Send Error : ",ex)        
        return False

def sendotp(request):
    email = request.GET.get("email")
    # select * from webapp_donor where email='ram@blood.com'
    records = Donor.objects.filter(email=email)
    if len(records)>0:
        # OTP Send
        rec = records[0]
        otp = generateOTP(5)
        check = sendmail(email,rec.name,otp)
        if check:
            request.session['loginotp'] = otp
            return HttpResponse("OTP Send Successfully !")
        else:
            return HttpResponse("OTP Send Failed, Please Try Again  !")           
    else:            
        return HttpResponse("Email Id Not Exist !")

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        otp = request.POST.get("otp")
        loginotp = request.session.get("loginotp")        
        if otp==loginotp:
            return HttpResponse("YES")
        else:
            return HttpResponse("No")            

def home(request):
    return render(request,"home.html")

def register(request):
    code = request.GET.get("err")
    msg = ""
    if code=="0":
        msg="Registeration Done !"
    if code=="1":
        msg="Phone or Email is Already Registered !"        
    if code=="2":
        msg="Registeration Failed !"        
    return render(request,"register.html",{"msg":msg})

def savedonor(request):
    code = 0
    try:
        donor = Donor()
        donor.name = request.POST.get('name')        
        phone = request.POST.get('phone')        
        if len(phone)==0:
            donor.phone = None
        else:
            donor.phone = phone    
        donor.email = request.POST.get('email')        
        donor.dob = request.POST.get('dob')        
        donor.group = int(request.POST.get('group'))
        donor.gender = int(request.POST.get('gender'))        
        donor.save()
    except IntegrityError as ex:        
        print("Save Donor Duplicate Error : ",ex)    
        code = 1
    except Exception as ex:    
        print("Save Donor Error : ",ex)    
        code = 2
    return redirect("/bloodbank/register?err="+str(code))    