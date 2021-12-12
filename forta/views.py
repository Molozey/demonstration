from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .SQL_db_test import *
from .forms import *
from .FIFA_def import FIFA

# Create your views here.
def main(request):
    companies = TickerInformation.objects.all()

    for company in companies:
       if company.logo_url == None:
           company.logo_url = 'https://www.dobro38.ru/upload/iblock/629/keg-20l.jpg'

    context = {'companies': companies}
    return render(request, 'base_main.html', context)

def company_info(request, pk):
     companies_info = TickerInformation.objects.filter(ticker=pk)
     companies_sector = TickerSector.objects.filter(ticker=pk)
     fifa_data_tick = list(FIFA(ticker_name=pk, columns=['market_cap', 'earnings', 'revenue_growth', 'price_to_earnings']).values())
     fifa_data = fifa_data_tick[1:]
     for company in companies_info:
         if company.logo_url == None:
             company.logo_url = 'https://www.dobro38.ru/upload/iblock/629/keg-20l.jpg'

     context = {'companies_info': companies_info, 'companies_sector': companies_sector, 'fifa_data': fifa_data}
     return render(request, 'base_comp_info.html', context)

