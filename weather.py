import requests

API_KEY = "d5220363c30180c3ea68f4e1dc16336f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # where we'll send request to : URL

city = input("Enter a city name : ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

# get data associate to the city
response = requests.get(request_url)

"""
meaning of the HTTP status code: (three digits long)
The HTTP status code determines whether the request made by the client has been successflly completed or not.
"""

if response.status_code == 200: # our request is OK
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 272.15, 2)
    count = data["sys"]["country"]
    city = data["name"]
    print("Country ", count, ", City ", city)
    print("Weather : ", weather)
    print("Temperature : ", temperature, "Celsius")
else:
    print("An error occurred !")

