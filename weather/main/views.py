import json
# import json to load json data to python dictionary 

from django.shortcuts import render

import urllib.request 
# urllib.request to make a request to api

# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q =' 
                    + city + '&appid = your_api_key_here').read() 
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source)
        
        data = {
            "country_code":str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        
        print(data)
        
    else:
        data ={}
    return render(request,"index.html",data)
