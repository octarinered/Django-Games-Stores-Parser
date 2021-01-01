from django.shortcuts import render
from django.http import HttpResponse
from parser_generator import initialize_parser

from .forms import searchGameForm

def HomePage(request):
    search = searchGameForm()

    if request.method == 'POST':

        game = request.POST.get('gameName')
        parsed_data = initialize_parser.get_price(game)

        data = {
            'game':game, 
            #----------------------------
            'epicgames_price': parsed_data['price']['epicgames'], 
            'playstationstore_price': parsed_data['price']['playstationstore'],
            'microsoftstore_price': parsed_data['price']['microsoftstore'],
            'steam_price': parsed_data['price']['steam'],
            #----------------------------
            'steampay_price':parsed_data['price']['steampay'], 
            'gabestore_price':parsed_data['price']['gabestore'],
            'icegames_price': parsed_data['price']['icegames'],
            'gamefarm_price': parsed_data['price']['gamefarm'],
            'steambuy_price': parsed_data['price']['steambuy'],
            #----------------------------
            #----------------------------
            #----------------------------
            'epicgames_link': parsed_data['link']['epicgames'],
            'playstationstore_link': parsed_data['link']['playstationstore'],
            'microsoftstore_link': parsed_data['link']['microsoftstore'],
            'steam_link': parsed_data['link']['steam'],
            #----------------------------
            'steampay_link':parsed_data['link']['steampay'], 
            'gabestore_link':parsed_data['link']['gabestore'],
            'icegames_link': parsed_data['link']['icegames'],
            'gamefarm_link': parsed_data['link']['gamefarm'],
            'steambuy_link': parsed_data['link']['steambuy'], 
            #----------------------------
            'form': search}

        return render(request, 'home.html', context=data)
    else:
        data = {'form': search}
        return render(request, 'home.html', context=data)
