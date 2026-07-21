import requests

def get_coordinates(city):
        
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

        try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                if "results" in data and data["results"]:
                        latitude = data["results"][0]["latitude"]
                        longitude = data["results"][0]["longitude"]
                        return latitude, longitude
                
        except requests.RequestException:
                print("Network or API error!")
        return None, None
        



def get_weather(latitude, longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        
        try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                
                temperature = data["current"]["temperature_2m"]
                temperature_unit = data["current_units"]["temperature_2m"]
                humidity = data["current"]["relative_humidity_2m"]
                humidity_unit = data["current_units"]["relative_humidity_2m"]
                wind_speed = data["current"]["wind_speed_10m"]
                wind_speed_unit = data["current_units"]["wind_speed_10m"]
                return temperature, temperature_unit, humidity, humidity_unit, wind_speed, wind_speed_unit
                
        except requests.RequestException:
                print("Error! While fetching the weather.")
                return None, None, None, None, None, None
        
        
        

        



                
        
         



