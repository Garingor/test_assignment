import uvicorn
from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi_utils.tasks import repeat_every
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from urllib.request import urlopen
import json

import crud
import models
import config
from database import SessionLocal, engine, SQLALCHEMY_DATABASE_URL


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
@repeat_every(seconds=60)
def test_print():
    db_string = SQLALCHEMY_DATABASE_URL
    con = create_engine(db_string)
    Session = sessionmaker(con)
    db = Session()

    cities_names = list(db.query(models.City.name).where(models.City.id.in_(
        db.query(func.max(models.City.id)).group_by(models.City.name))))

    for city_name in cities_names:
        response = urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city_name[0] + "&units=metric&appid=" +
                           config.OPEN_WEATHER_MAP_API_KEY)
        data = json.loads(response.read())

        if len(data) == 2 and data['cod'] == config.WRONG_CITY_NAME:
            return None
        else:
            db_city = models.City(name=city_name[0], temperature=data['main']['temp'],
                                  atmosphere_pressure=data['main']['pressure'],
                                  wind_speed=data['wind']['speed'])
            db.add(db_city)
            db.commit()
            db.refresh(db_city)


@app.get("/last_weather/")
def get_last_weather(city_name: str | None = Query(default=None, alias="search"),
                     db: Session = Depends(get_db)):
    if city_name:
        weather_info = crud.get_last_city_weather(db, city_name=city_name)
    else:
        weather_info = crud.get_last_cities_weather(db)

    if not list(weather_info):
        raise HTTPException(status_code=404, detail="Weather info not found.")

    return weather_info


@app.get("/city_stats/")
def get_city_stats(city_name: str | None = Query(default=None, alias="search"),
                   minutes: str | None = Query(default=None, alias="minutes"),
                   db: Session = Depends(get_db)):
    if city_name:
        weather_info = crud.get_city_stats(db, city_name, minutes)
    else:
        raise HTTPException(status_code=404, detail="Weather info not found.")

    if not list(weather_info):
        raise HTTPException(status_code=404, detail="Weather info not found.")

    return weather_info


@app.post("/weather/{city}")
def post_city(city: str, db: Session = Depends(get_db)):
    new_city = crud.add_city(db, city=city)
    print(new_city)
    if new_city is None:
        raise HTTPException(status_code=404, detail="City not found.")

    return "city " + city + " added successfully"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)  # параметры запуска
