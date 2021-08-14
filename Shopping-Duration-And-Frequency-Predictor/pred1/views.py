from django.shortcuts import render
from django.http import HttpResponse
from . import shopping_duration

# Create your views here.

def home(request):
    return render(request, 'index.html')

def duration_render(request):
    return render(request, 'predict_shopping_duration.html')

def amount_render(request):
    return render(request, 'predict_shopping_amount.html')

    
def duration_predict(request):
    
    weekday = {
        "monday": 1, "tuesday": 2, "wednesday":3, "thursday":4, "friday":5, "saturday":6
    }

    attendants = {
        "no":1, "family":2, "life partner":3, "family member":4, "little child":5
    }

    val1 = request.POST['num1']
    val2 = request.POST['num2']
    val3 = request.POST['num3']
    val4 = request.POST['num4']
    val5 = request.POST['num5']
    val6 = request.POST['num6']
    val7 = request.POST['num7']
    val8 = request.POST['num8']
    val9 = request.POST['num9']
    val10 = request.POST['num10']
    val11 = request.POST['num11']

    res = shopping_duration.predict_shopping_duration([val1,val2,val3,val4,val5,val6,val7,weekday[val8],attendants[val9],val10,val11])

    return render(request, "predict_shopping_duration.html", {'result':res})

def amount_predict(request):
    
    weekday = {
        "monday": 1, "tuesday": 2, "wednesday":3, "thursday":4, "friday":5, "saturday":6
    }

    attendants = {
        "no":1, "family":2, "life partner":3, "family member":4, "little child":5
    }

    val1 = request.POST['num1']
    val2 = request.POST['num2']
    val3 = request.POST['num3']
    val4 = request.POST['num4']
    val5 = request.POST['num5']
    val6 = request.POST['num6']
    val7 = request.POST['num7']
    val8 = request.POST['num8']
    val9 = request.POST['num9']
    val10 = request.POST['num10']
    val11 = request.POST['num11']

    dick = {
        1:"less", 2:"normal", 3:"bag full", 4:"heavy"
    }

    res = shopping_duration.predict_shopping_amount([val1,val2,val3,val4,val5,val6,val7,weekday[val8],attendants[val9],val10,val11])
    res2 = dick[res[0]]

    return render(request, "predict_shopping_amount.html", {'result':res2})
