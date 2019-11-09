#!/usr/bin/env python3

import requests, json, os
from datetime import date

api_key = "79fb1e0e0654b11e1319112ffe57fba4"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()



if x["cod"] != "404":
	y = x["main"]
	current_temp = int(y["temp"] - 273.15)
	current_pressure = y["pressure"]
	current_humidity = y["humidity"]

	z = x["weather"]

	weather_description = z[0]["description"]

	os.system('cls' if os.name == 'nt' else 'clear')
	print("The temperature is currently", current_temp, "degrees Celsius")
	print("The air pressure is currently", current_pressure)
	print("The humidity is currently", current_humidity, "percent")
	print("The weather is currently", weather_description)
	print(json.dumps(x, indent=2, sort_keys=True))
	print(date.today())
else:
	print("City not found.")
