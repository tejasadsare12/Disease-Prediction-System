import django
from django.shortcuts import render
from django.contrib import messages
from webapp.models import Symptoms,users
import webapp.prediction.prediction

from webapp import views

def ind(request):
    return render(request, 'webapp/index.html')

def signup(request):
    if request.method == "POST":
        formtype = request.POST.get('formtype')

        if(formtype == "login"):
            email = request.POST.get('email')
            password = request.POST.get('password')

            if (email == "" or password == "" ):
                messages.info(request, 'Please Enter All fields')

            else:
                data = users.objects.all()
                if(data != ""):
                    for i in data:
                        i1 = str(i)
                        if(i1 == email):
                            messages.success(request, 'Login Successfull')
                            return django.shortcuts.redirect('/prediction/')
                        else:
                            messages.info(request, 'Please Enter Correct Credentials')
                else:
                    print("no data")


        elif(formtype == "signup"):
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            if (username == "" or email == "" or password == "" or phone == ""):
                messages.info(request, 'Please Enter All fields')
            else:
                user_email = users.objects.filter(email=email)
                if user_email:

                    for eml in user_email:
                        eml_str = str(eml)
                        if(email == eml_str):
                            messages.info(request, 'User Already Exists')
                        else:
                            userData = users(name=username, email=email, phone=phone, password=password)
                            userData.save()
                            messages.success(request, 'User Created Succesfully')
                else:
                    userData = users(name=username, email=email, phone=phone, password=password)
                    userData.save()

                    messages.success(request, 'User Created Succesfully')

    return render(request, 'webapp/signup.html')

def prediction(request):
    context = {
        'symptoms': webapp.prediction.prediction.l1
    }
    if request.method == "POST":
        symp1 = request.POST.get('symp1')
        symp2 = request.POST.get('symp2')
        symp3 = request.POST.get('symp3')
        symp4 = request.POST.get('symp4')
        symp5 = request.POST.get('symp5')

        if (symp1 == "null" or symp2 == "null" or symp3 == "null" or symp4 == "null" or symp5 == "null"):
            messages.info(request, 'All Sympotms are Not Selected, Please Select The Symptoms')
        else:
            userSymtomps = Symptoms(symp1=symp1, symp2=symp2, symp3=symp3, symp4=symp4, symp5=symp5)
            userSymtomps.save()

            symptom_list = [symp1, symp2, symp3, symp4, symp5]
            result = webapp.prediction.prediction.NaiveBayes(symptom_list)
            resultDict = {
                'PredictedDisease': result,
                'symptoms': webapp.prediction.prediction.l1,
                'userSymptoms': symptom_list
            }
            return render(request, 'webapp/prediction.html', resultDict)
    return render(request, 'webapp/prediction.html', context)

def redirect_view(request):
    response = django.shortcuts.redirect('/redirect-success/')
    return response
