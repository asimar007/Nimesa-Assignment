import requests

api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None

def get_weather_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None

def get_wind_speed_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None

def get_pressure_by_date(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None

if __name__ == "__main__":
    weather_data = get_weather_data()

    if weather_data is not None:
        while True:
            print("\nOptions:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")

            choice = input("Enter your choice:- ")

            if choice == '1':
                date = input("Enter Date (YYYY-MM-DD HH:MM:SS): ")
                temperature = get_weather_by_date(weather_data, date)
                if temperature is not None:
                    print(f"Temperature on {date}: {temperature} K")
                else:
                    print("Data not available.")

            elif choice == '2':
                date = input("Enter Date (YYYY-MM-DD HH:MM:SS): ")
                wind_speed = get_wind_speed_by_date(weather_data, date)
                if wind_speed is not None:
                    print(f"Wind Speed on {date}: {wind_speed} m/s")
                else:
                    print("Data not available.")

            elif choice == '3':
                date = input("Enter Date (YYYY-MM-DD HH:MM:SS): ")
                pressure = get_pressure_by_date(weather_data, date)
                if pressure is not None:
                    print(f"Pressure on {date}: {pressure} hPa")
                else:
                    print("Data not available.")

            elif choice == '0':
                print("Exit")
                break

            else:
                print("Invalid choice")
