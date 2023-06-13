from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class City(Base):  # SQLAlchemy извлекает элементы из БД и заполняет по шаблону -->
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    temperature = Column(Integer, index=True)
    atmosphere_pressure = Column(Integer, index=True)
    wind_speed = Column(Integer, index=True)
