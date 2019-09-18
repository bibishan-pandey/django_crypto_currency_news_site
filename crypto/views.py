from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    # Grab crypto price data
    price_api_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,LTC,USDT,EOS,BNB,BSV,XLM&tsyms=USD")
    price_api = json.loads(price_api_request.content)

    # Grab crypto news
    news_api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news_api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'news_api': news_api, 'price_api': price_api})


def prices(request):
    if request.method == 'POST':
        import requests
        import json

        # Grab crypto price data
        quote = request.POST['quote']
        quote = quote.upper()
        if quote == '':
            notfound = "Enter crypto currency in the search bar above..."
            return render(request, 'prices.html', {'notfound': notfound})
        crypto_api_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto_api = json.loads(crypto_api_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto_api': crypto_api})
    else:
        notfound = "Enter crypto currency in the search bar above..."
        return render(request, 'prices.html', {'notfound': notfound})
