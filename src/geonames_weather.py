import os
import requests


class GeoNames:
    def __init__(self, username):
        self.base_url = "http://api.geonames.org/searchJSON"
        self.username = os.getenv("GEONAME_USERNAME")

    def get_coordinates(self, city_name):
        params = {
            'q': city_name,
            'maxRows': 1,
            'username': self.username
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['totalResultsCount'] > 0:
                lat = round(float(data['geonames'][0]['lat']), 4)
                lng = round(float(data['geonames'][0]['lng']), 4)
                return lat, lng
        return None, None
