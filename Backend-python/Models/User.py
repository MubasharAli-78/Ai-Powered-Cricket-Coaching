from sqlalchemy import String, Integer, Column,Enum
from sqlalchemy.orm import relationship
from config import Base

class User(Base):
    __tablename__ = 'User'

    id =Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    role = Column(String(25), nullable=False)
    username = Column(String(25), nullable=False)
    password = Column(String(20), nullable=False)
    experience = Column(Integer, nullable=False)
    date_of_birth = Column(String(12), nullable=False)
    contact_no = Column(String(20), nullable=False)
    type = Column(String(25), nullable=True)
    is_team_assigned= Column(String(10), default='0',nullable=True)
    is_active= Column(String(10), default='1',nullable=True)

    session = relationship("Session", foreign_keys="Session.coach_id", back_populates="coach")
    session_Player = relationship("SessionPlayer", foreign_keys="SessionPlayer.player_id", back_populates="player")
    team_Coach = relationship("TeamCoach", back_populates="user")
    team_Manager = relationship("TeamManager", back_populates="user")
    team_Player = relationship("TeamPlayer", back_populates="user")

