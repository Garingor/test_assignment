from sqlalchemy.orm import Session
from sqlalchemy import func
from urllib.request import urlopen
import json

import models
import config


def get_last_cities_weather(db: Session):
    return db.query(models.City.name, models.City.temperature).where(models.City.id.in_(
        db.query(func.max(models.City.id)).group_by(models.City.name)))

    # select name, temperature from cities where id in (select max(id) from cities group by name)


def get_last_city_weather(db: Session, city_name: str):
    return db.query(models.City.name, models.City.temperature).where(models.City.id.in_(
        db.query(func.max(models.City.id)).group_by(models.City.name))).filter(models.City.name == city_name)

    # select temperature from cities
    # where id in (select max(id) from cities where cities.name = city_name group by name)


def get_city_stats(db: Session, city_name: str, minutes: str):
    cities = list(db.query(models.City).filter(models.City.name.like('%' + city_name + '%')))

    # select temperature from cities where like '%city_name%'

    if not cities:  # проверка на пустой ответ
        return cities

    minutes = round(int(minutes))  # выбранный период (в минутах)

    if int(minutes) > len(cities):  # если выбранный период больше кол-во записей в бд
        minutes = len(cities)

    cities = cities[-minutes:]  # взять записи с конца

    temperature_avg = 0
    atmosphere_pressure_avg = 0
    wind_speed_avg = 0

    for city in cities:  # подсчет средних значений
        temperature_avg += city.temperature
        atmosphere_pressure_avg += city.atmosphere_pressure
        wind_speed_avg += city.wind_speed

    temperature_avg /= len(cities)
    atmosphere_pressure_avg /= len(cities)
    wind_speed_avg /= len(cities)

    return [cities, {"temperature_avg": round(temperature_avg, 3)},  # округление до 3-х значащих чисел
            {"atmosphere_pressure_avg": round(atmosphere_pressure_avg, 3)},
            {"wind_speed_avg": round(wind_speed_avg, 3)}]


def add_city(db: Session, city: str):
    try:
        response = urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" +
                           config.OPEN_WEATHER_MAP_API_KEY)  # API для получения погоды (в json)
    except:
        return None

    data = json.loads(response.read())  # преобразовать JSON в словарь

    if len(data) == 2 and data['cod'] == config.WRONG_CITY_NAME:  # проверка на корректность API реквеста
        return None
    else:
        db_city = models.City(name=city, temperature=data['main']['temp'], atmosphere_pressure=data['main']['pressure'],
                              wind_speed=data['wind']['speed'])
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
        return db_city
