#this is a weather app which uses an api to get current weather
# importing geopy library
import requests
import json

# entering the location name
city = input("Enter name of city : ")

url = f"http://api.weatherapi.com/v1/current.json?key=fc960bef45474075bcf73003233007&q={city}&aqi=no"

r = requests.get(url)
#print(r.text)
dic = json.loads(r.text)
print(dic)
print()
print("temp in degree celcius : ",dic['current']['temp_c'])