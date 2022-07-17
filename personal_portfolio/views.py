from django.shortcuts import render
from portfolio.models import Project, Product
import requests
from datetime import datetime


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def currency(request):
    cryptos = ['BTC', 'ETH', 'XRP', 'BNB', 'ADA', 'SOL', 'DASH', 'DOGE', 'XMR']
    dictionary = requests.get(f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={','.join(cryptos)}&tsyms=USD").json()
    values = [dictionary[cryp]['USD'] for cryp in cryptos]
    diction = dict(zip(cryptos, values))
    date_time = datetime.now(tz=None).strftime("%b %d %Y %H:%M:%S")
    return render(request, 'portfolio/currency.html', {'context': diction, 'date': date_time})


def price_history(request):
    products = Product.objects.all()
    result_dict = {}
    for product in products:
        url = f"https://catalog.api.onliner.by/products/{product.code}/prices-history"
        date_time_dict = requests.get(url=url).json()['chart_data']['items'][-15:-1]
        for item in date_time_dict:
            if not item['price']:
                item['price'] = 'Out of stock'
        result_dict[product.name] = (product.code, product.manufacturer, product.category, date_time_dict)
    return render(request, 'portfolio/price_history.html', {'context': result_dict})
