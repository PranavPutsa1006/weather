def weather(loc="your city"):
    # returns current location's weather conditions like cloud coverage, temperature, humidity and wind speed
    owm = pyowm.OWM('your pyowm api id')
    country_code = 'your country's code'
    obs = owm.weather_at_place(loc + "," + country_code)
    w = obs.get_weather()
    weathers = {'cloud_coverage': w.get_clouds(), 'wind': w.get_wind(), 'humidity': w.get_humidity(), 'temp': w.get_temperature(unit='celsius')}
    cloud_coverage = ''
    wind_speed = weathers['wind']['speed']
    humidity = weathers['humidity']
    temp_cur = weathers['temp']['temp']
    # the following lines give the corresponding cloud coverage according to cloud_coverage percentage
    if weathers['cloud_coverage'] in range(0, 11):
        cloud_coverage = 'clear sky'
    elif weathers['cloud_coverage'] in range(11, 51):
        cloud_coverage = 'scattered clouds'
    elif weathers['cloud_coverage'] in range(51, 91):
        cloud_coverage = 'broken clouds'
    elif weathers['cloud_coverage'] in range(91, 101):
        cloud_coverage = 'overcast clouds'
    return temp_cur, cloud_coverage, humidity, wind_speed
