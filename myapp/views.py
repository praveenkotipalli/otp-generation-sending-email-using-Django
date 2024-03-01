import random
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def send_email(subject, body, recipient):
    # Your email sending logic here
    print(f"Email sent to {recipient} with subject: {subject}")

# Now you can call the send_email function
send_email("Hello", "This is the body of the email", "example@example.com")

def home(request):
    if request.method == 'POST':
        length= int(request.POST['length'])
        otp = ""
        for _  in range(length):
            otp+=str(random.randint(0,9))
        comment = "Welcome to Travel Tour"
        comment1 = comment + otp
        # send_email(
        #     'OTP for Travel Tour',
        #     comment1,
        #     settings.EMAIL_HOST_USER,
        #     ['praveenin321@gmail.com'],
        #     recipient_list=['2200032132@kluniversity.in'],
        #     fail_silently=False,
        # )
        return render(request,'index.html',{'otp': otp})

    return render(request, 'home.html')