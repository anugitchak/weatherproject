from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
       city =request.POST['city']
       res =urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=723e1976a8dd5fe79c19e52be944b453').read()
       json_data = json.loads(res)
       data ={
        "country_code": str(json_data['sys']['country']),
        "coordinate": str(json_data['coord']['lon']) +' '+str(json_data['coord']['lat']),
        "temp" : str(json_data['main']['temp']) +'k',
        "Pressure": str(json_data['main']['pressure']),
        "humidity": str(json_data['main']['humidity']),
        'icon': str(json_data['weather'][0]['icon'])
       }

    else:
        city =''
        data ={}   
    return render(request,'index.html' ,{'city': city,'data':data})
