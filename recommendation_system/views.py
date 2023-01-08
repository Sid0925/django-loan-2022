from django.shortcuts import render
 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import numpy as np;
from sklearn.ensemble import RandomForestClassifier;
from sklearn.preprocessing import StandardScaler;
import joblib;
import os;
import pickle;
# Create your views here.

def home(request):
    return render(request,'index.html')


def system(request):
    return render(request,'system.html')

def print_result(request):
    Gender =  request.POST["gender"]
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    married = request.POST["Married"]
    if married == 'Yes':
        married = 1
    else:
        married = 0

    employed = request.POST["employed"]
    if employed == 'Yes':
        employed = 1
    else:
        employed = 0
    
    eduction = request.POST["eduction"]
    if eduction == 'Yes':
        eduction = 1
    else:
        eduction = 0

    dependant = request.POST["depedent"]
    dependant1 = 0
    dependant2 = 0
    dependant3 = 0

    if dependant == 1:
        dependant1 = 1
        dependant2 = 0
        dependant3 = 0
    elif dependant ==2:
        dependant1 = 0
        dependant2 = 1
        dependant3 = 0
    elif dependant ==3:
        dependant1 = 0
        dependant2 = 0
        dependant3 = 1


    Property_Area_Semiurban	= 0
    Property_Area_Urban = 0

    property = request.POST["property"]
    if property == 'Urban':
        Property_Area_Semiurban	= 0
        Property_Area_Urban = 1
    elif property == 'Semiurban':
        Property_Area_Semiurban	= 1
        Property_Area_Urban = 0


    amount =  int(request.POST["loan"])
    applicant_income = int(request.POST["aincome"])
    co_applicant_income = int(request.POST["cincome"])
    term =  int(request.POST["term"])

    credit = request.POST["credit"]
    if credit == 'Yes':
        credit = 1
    else:
        credit = 0

    scaler =  joblib.load('scaler_.pkl','r')
    new_applicant = scaler.transform([[Gender,married,dependant1,dependant2,dependant3,eduction,employed,
    Property_Area_Semiurban,Property_Area_Urban,
    applicant_income,co_applicant_income,term,amount,credit,applicant_income]])


    Model = joblib.load('Random forest model_.pkl')
    prediction = Model.predict(new_applicant)

    prediction = np.squeeze(prediction)


    if prediction ==  1:
        return render(request,'yes.html',{'am':amount} )
    else:
        return render(request,'print.html',{'am':amount} )

    