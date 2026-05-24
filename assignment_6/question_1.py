#1) Study the open weather API show more data in your API calling program
import requests
def weather_data(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9f8ed6e42ff0d0599844ff1fae482446&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        print(f"""Maximum Temprature:{data['main']['temp_max']}
Minimum Temprature:{data['main']['temp_min']}
Average Temprature:{data['main']['temp']}""")
        

    except requests.exceptions.RequestException as e:
        print(e)


city=input("Enter your city:")

weather_data(city)


