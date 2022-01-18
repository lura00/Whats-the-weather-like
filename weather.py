import requests
import time
from datetime import datetime
from database import weather_cloud

today = datetime.today().strftime('%Y-%m-%d')

db = weather_cloud()


# def get_weather():
api = f"http://api.openweathermap.org/data/2.5/weather?q=Stockholm&units=metric&appid=aee454f3fe00a9f1f321d2b4376a4bd1"
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = json_data['main']['temp']
min_temp = json_data['main']['temp_min']
max_temp = json_data['main']['temp_max']
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']
sunrise = time.strftime(
    "%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

# final_info = condition + "\n" + str(temp) + "°C"
# final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(
#     pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sundown: " + sunset
weather_list = (condition, str(temp) + "°C", "Max Temp: " + str(max_temp), "Min Temp: " +
                str(min_temp), "Wind Speed: " + str(wind), "Sunrise: " + sunrise, "Sundown: " + sunset, today)
# return condition, temp, max_temp, min_temp, wind, sunrise, sunset


# weather_history = get_weather(), today
# print(weather_list[0])
db.insert_data(weather_list)
db.show_all()
# db.insert_data(weather_history, today)
