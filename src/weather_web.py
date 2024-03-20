import os
from src.geonames_weather import GeoNames
from src.weather_api import YrWeatherAPI
from src.reformat_weather_time import extract_current_weather


def get_weather(city_name):
    geonames = GeoNames(username=os.getenv("GEONAME_USERNAME"))
    lat, lon = geonames.get_coordinates(city_name)

    if not lat or not lon:
        return None, "Kunne ikke finne koordinatene for byen."

    api = YrWeatherAPI()
    weather_data = api.get_weather_data(lat, lon)

    if not weather_data:
        return None, "Ingen værdata funnet."

    weather = extract_current_weather(weather_data)
    if not weather:
        return None, "Ingen aktuell værdata tilgjengelig."

    return weather, None
