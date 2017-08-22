# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from random import randrange

# Create your views here.
def index(request):
    context = {}
    try:
        thisGold = request.session['gold']
        activity_Strings = request.session['activity']
    except Exception as e:
        print "reset gold, exception"
        request.session['gold'] = 200
        request.session['activity'] = []
    else:
        pass
    return render(request, "NinjaGold_app/index.html")

def process_money(request):
    bld = request.POST['building']
    if bld == "farm":
        newGold = randrange(-10, 20)
        request.session['gold'] += newGold
        newTotal = request.session['gold']
        print newGold, newTotal, str(newGold), str(newTotal)
        if newGold < 1:
            request.session['activity'].append("<div class='red'>Farmed a bit for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
        else:
            request.session['activity'].append("<div class='tan'> Farmed a bit for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
    elif bld == "cave":
        newGold = randrange(-5, 10)
        request.session['gold'] += newGold
        newTotal = request.session['gold']
        if newGold < 1:
            request.session['activity'].append("<div class='red'>Spulunked a cave for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
        else:
            request.session['activity'].append("<div class='tan'>Spulunked a cave for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
    elif bld == "house":
        newGold = randrange(-2, 5)
        request.session['gold'] += newGold
        newTotal = request.session['gold']
        if newGold < 1:
            request.session['activity'].append("<div class='red'>Rented a house for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
        else:
            request.session['activity'].append("<div class='tan'>Rented a house for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
    elif bld == "casino":
        newGold = randrange(-50, 30)
        request.session['gold'] += newGold
        newTotal = request.session['gold']
        if newGold < 1:
            request.session['activity'].append("<div class='red'>Gambled for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
        else:
            request.session['activity'].append("<div class='tan'>Gambled for $" + str(newGold) + " gold.  Total: " + str(newTotal) + "</div>")
    # else:
    return redirect('/')

def reset(request):
    try:
        del request.session['gold']
    except Exception as e:
        pass
    try:
        del request.session['activity']
    except Exception as e:
        pass
    return redirect('/')
