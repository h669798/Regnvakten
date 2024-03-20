import os
from src.geonames_weather import GeoNames
from src.reformat_weather_time import extract_current_weather
from src.weather_api import YrWeatherAPI

def main():
    geonames = GeoNames(username=os.getenv("GEONAME_USERNAME"))
    city_name = input("Skriv inn bynavn: ")
    lat, lon = geonames.get_coordinates(city_name)

    if lat and lon:
        api = YrWeatherAPI()
        weather_data = api.get_weather_data(lat, lon)
        extract_current_weather(weather_data)
    else:
        print("Kunne ikke finne koordinatene for byen.")


if __name__ == "__main__":
    main()
