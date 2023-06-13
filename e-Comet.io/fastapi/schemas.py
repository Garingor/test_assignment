from pydantic import BaseModel


class City(BaseModel):
    name: str
    temperature: int
    atmosphere_pressure: int
    wind_speed: int
    