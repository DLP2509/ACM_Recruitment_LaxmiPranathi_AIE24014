import http.client
import json
conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "b28468cb4cmsh70ba00fdbc23ff0p1bd03djsna385e8108912",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com"
}
conn.request("GET", "/city/landon/EN", headers=headers)
res = conn.getresponse()
if res.status == 200:
    
    data = res.read().decode("utf-8")
    
    parsed_data = json.loads(data)
    
    main = parsed_data.get('main', {})
    wind = parsed_data.get('wind', {})
    clouds = parsed_data.get('clouds', {})
    weather = parsed_data.get('weather', [{}])[0] 

    temp = main.get('temp') - 273.15 
    temp_min = main.get('temp_min') - 273.15
    temp_max = main.get('temp_max') - 273.15

    print("Weather Information:")
    print(f"Temperature: {temp:.2f}°C")
    print(f"Temperature (Min): {temp_min:.2f}°C")
    print(f"Temperature (Max): {temp_max:.2f}°C")
    print(f"Humidity: {main.get('humidity', 'N/A')}%")
    print(f"Pressure: {main.get('pressure', 'N/A')} hPa")
    print(f"Sea Level Pressure: {main.get('sea_level', 'N/A')} hPa")
    print(f"Ground Level Pressure: {main.get('grnd_level', 'N/A')} hPa")
    print(f"Weather Description: {weather.get('description', 'N/A')}")
    print(f"Wind Speed: {wind.get('speed', 'N/A')} m/s")
    print(f"Cloud Coverage: {clouds.get('all', 'N/A')}%")
else:
    print(f"Error: {res.status} {res.reason}")

conn.close()
