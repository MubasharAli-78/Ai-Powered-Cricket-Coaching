from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from config import Base


class Team(Base):
    __tablename__ = 'Team'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=True)


    team_Coach = relationship("TeamCoach", back_populates="team")
    team_Player = relationship("TeamPlayer", back_populates="team")
    team_Manager = relationship("TeamManager", back_populates="team")
