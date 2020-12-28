from django.shortcuts import render
from django.http import HttpResponse
from parser_generator import initialize_parser

from .forms import searchGameForm

def HomePage(request):
    search = searchGameForm()

    if request.method == 'POST':

        game = request.POST.get('gameName')
        price = initialize_parser.get_price(game)

        data = {
            'game':game, 
            #----------------------------
            'epicgames_price': price['epicgames'], 
            'playstationstore_price': price['playstationstore'],
            'microsoftstore_price': price['microsoftstore'],
            'steam_price': price['steam'],
            #----------------------------
            'steampay_price':price['steampay'], 
            'gabestore_price':price['gabestore'],
            'icegames_price': price['icegames'],
            'gamefarm_price': price['gamefarm'],
            'steambuy_price': price['steambuy'],
            #----------------------------
            'form': search}

        return render(request, 'home.html', context=data)
    else:
        data = {'form': search}
        return render(request, 'home.html', context=data)
