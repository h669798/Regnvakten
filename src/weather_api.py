import requests


class YrWeatherAPI:
    def __init__(self):
        self.base_url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
        self.headers = {"User-Agent": "Regnvakten github.com/h669798/Regnvakten"}
        self.last_modified = None

    def get_weather_data(self, lat, lon):
        parameters = {"lat": lat, "lon": lon}
        if self.last_modified:
            self.headers["If-Modified-Since"] = self.last_modified

        response = requests.get(self.base_url, headers=self.headers, params=parameters)

        if response.status_code == 200:
            self.last_modified = response.headers.get("Last-Modified", "")
            return response.json()
        elif response.status_code == 304:
            print("Data ikke endret siden sist.")
            return None
        else:
            response.raise_for_status()

