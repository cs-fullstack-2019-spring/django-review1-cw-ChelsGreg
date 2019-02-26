from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cocktails

# Create your views here.

# FUNCTIONS FOR PAGE, PAGES
def home(request):

    return render(request, 'rev1App/home.html')

def page2(request):
    return render(request, 'rev1App/page2.html')


def page3(request):
    return render(request, 'rev1App/page3.html')


def page4(request):
    return render(request, 'rev1App/page4.html')


def page5(request):
    return render(request, 'rev1App/page5.html')



# FUNCTION TO DISPLAY EACH COCKTAIL NAME
def cocktails(request):
    drinks = Cocktails.objects.all()
    context ={
        'drinkThis': drinks
    }

    return render(request, 'rev1App/cocktails1.html', context)

# FUNCTION TO LINK DETAIL PAGE TO MAIN PAGE AND DISPLAY NAME
def cocktails2(request, drinkID):
    drink = get_object_or_404(Cocktails, pk=drinkID)
    context={
        'drinks': drink
    }


    return render(request, 'rev1App/cocktails2.html', context)
