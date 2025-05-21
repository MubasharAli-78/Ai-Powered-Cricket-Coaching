from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class ShotResult(Base):
    __tablename__ = 'ShotResult'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_shot_id = Column(Integer, ForeignKey('SessionShot.id'), nullable=False)
    is_shot_correct = Column(Integer, nullable=False)


    session_shot = relationship("SessionShot", back_populates="shot_result")
