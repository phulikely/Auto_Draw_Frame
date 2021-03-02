from get_weather import Get_Weather
import pytest


def test_valid_city_in_country():
	get_weather = Get_Weather()
	city = 'Hưng Yên'

	resp = get_weather.get_city_weather(city)
	assert city in resp["name"]
	assert resp["temp"] != None
	assert resp["humidity"] != None


def test_invalid_city():
	get_weather = Get_Weather()
	city = 'xyz'

	resp = get_weather.get_city_weather(city)
	assert resp == None