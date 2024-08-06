# Weather api request
import requests
# from pprint import pprint


def get_temp(city):
    API_key = 'e47a270fe3a33a7fe2f42131261ecbea'


    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'

    response = requests.get(url)

    data = response.json()
    kelvin_temp = data['main']['temp']

    return kelvin_temp

def convert_temp(temp):
    cel_temp = round((temp - 273.15),2)
    return cel_temp

    

def main():
    city =  input("Please enter your city: ")
    raw_temp = get_temp(city)
    temp = convert_temp(raw_temp)
    print(f'Current temperature in {city} is: {temp} 🌤️')













main()




