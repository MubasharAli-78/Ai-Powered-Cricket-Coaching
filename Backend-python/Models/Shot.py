from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from config import Base


class Shot(Base):
    __tablename__ = 'Shot'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))


    shot_ideal_angle = relationship('ShotIdealAngle', back_populates='shot')
    session_Shot = relationship("SessionShot", back_populates="shot")
