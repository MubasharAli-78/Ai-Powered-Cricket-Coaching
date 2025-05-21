from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Session(Base):
    __tablename__ = "Session"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    coach_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    date = Column(String(10), nullable=True)
    start_time = Column('session_from', String(20), nullable=True)
    end_time = Column('session_to', String(20), nullable=True)
    venue = Column(String(30), nullable=True)


    session_player = relationship("SessionPlayer", foreign_keys="SessionPlayer.session_id", back_populates="session")
    coach = relationship("User", foreign_keys=[coach_id], back_populates="session")
