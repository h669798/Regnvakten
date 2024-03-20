from django.shortcuts import render
from src.weather_web import get_weather


def weather_view(request):
    context = {'weather': None, 'error': None}

    if request.method == 'POST':
        city_name = request.POST.get('city_name', '')
        weather_data, error = get_weather(city_name)

        if error:
            context['error'] = error
        else:
            context['weather'] = weather_data

    return render(request, 'RegnvaktenApp/home.html', context)
