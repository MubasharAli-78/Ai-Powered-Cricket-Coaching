from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from config import Base


class Angle(Base):
    __tablename__ = 'Angle'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    angleLines = relationship("AngleLine", back_populates="angle")
    shot_ideal_angle = relationship("ShotIdealAngle", back_populates="angle")
