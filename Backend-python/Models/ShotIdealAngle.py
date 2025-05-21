from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class ShotIdealAngle(Base):
    __tablename__ = 'ShotIdealAngle'

    id = Column(Integer, primary_key=True, autoincrement=True)
    angle_name_id = Column(Integer, ForeignKey("Angle.id"), nullable=False)
    shot_id = Column(Integer, ForeignKey("Shot.id"), nullable=False)
    angle_from = Column(Integer)
    angle_to = Column(Integer)


    angle = relationship('Angle', back_populates='shot_ideal_angle')
    shot = relationship('Shot', back_populates='shot_ideal_angle')
