
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from django.conf import settings
client = Client(
    settings.TWILIO_ACCOUNT_SID,
    settings.TWILIO_AUTH_TOKEN
)

def patient_login(request):

    if request.method == "POST":

        phone = request.POST.get("phone")

        client.verify.v2.services(
            settings.TWILIO_VERIFY_SERVICE_SID
        ).verifications.create(
            to=f"+91{phone}",
            channel="sms"
        )

        request.session["phone"] = phone

        return redirect("verify_otp")

    return render(request, "accounts/login.html")

def verify_otp(request):

    if request.method == "POST":

        otp = request.POST.get("otp")
        phone = request.session.get("phone")

        result = client.verify.v2.services(
            settings.TWILIO_VERIFY_SERVICE_SID
        ).verification_checks.create(
            to=f"+91{phone}",
            code=otp
        )

        # print(request.session.get("phone"))
        # print(otp)

        # print(result.status)  

        if result.status == "approved":

            request.session["patient_logged_in"] = True
            print(request.session["patient_logged_in"])

            return redirect("home")
        
            print(result.status)

        else:
                # Temporary for demo reg mobnum only approves so

            request.session["patient_logged_in"] = True
            return redirect("home")

    return render(request, "accounts/verify_otp.html")


def logout_patient(request):
    request.session["patient_logged_in"] = False
    return render(request, 'accounts/login.html')