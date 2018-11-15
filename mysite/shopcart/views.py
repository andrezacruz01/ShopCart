from django.shortcuts import render
from mysite.models import SellObjects
from django.shortcuts import redirect
from mysite.models import Creditcard
from django.views.generic.base import View
from shopcart.form import RegisterCreditCardForm

# Create your views here.
def index(request):
    return render(request, 'index.html',
                  {'sellObjects': SellObjects.objects.all()})


class RegisterCreditcardView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')

    def post(self, request, *args, **kwargs):
        form = RegisterCreditCardForm(request.POST)

        if form.is_valid():
            data_form = form.data

            creditcard = Creditcard(name = data_form['name'],
                                    number = data_form['number'],
                                    date = data_form['date'],
                                    safety_key = data_form['safety_key'])

            creditcard.save()

            return redirect('index')

        return render(request, 'cart.html', {'form': form})