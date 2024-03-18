from data.weather_descriptions import descriptions
from datetime import datetime, timezone


def extract_current_weather(weather_data):
    now = datetime.now(timezone.utc)
    closest_time = None
    closest_weather = None

    for entry in weather_data['properties']['timeseries']:
        entry_time = datetime.fromisoformat(entry['time'].replace('Z', '+00:00'))
        if closest_time is None or abs(entry_time - now) < abs(closest_time - now):
            closest_time = entry_time
            closest_weather = entry

    if closest_weather:
        temperature = closest_weather['data']['instant']['details']['air_temperature']
        cloud_area_fraction = closest_weather['data']['instant']['details']['cloud_area_fraction']
        weather_symbol = closest_weather.get('data', {}).get('next_1_hours', {}).get('summary', {}).get('symbol_code', 'N/A')

        weather_description = descriptions.get(weather_symbol, "ukjent vær")

        print(f"Temperatur: {temperature}°C")
        print(f"Vær: {weather_description}")
    else:
        print("Ingen data.")

