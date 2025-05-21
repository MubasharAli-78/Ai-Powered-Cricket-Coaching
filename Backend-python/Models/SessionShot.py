from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import relationship
from config import Base


class SessionShot(Base):
    __tablename__ = "SessionShot"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_player_id = Column(Integer, ForeignKey('SessionPlayer.id'), nullable=False)
    shot_id = Column(Integer, ForeignKey('Shot.id'), nullable=False)


    session_player = relationship("SessionPlayer", back_populates="session_Shot")
    shot = relationship("Shot", back_populates="session_Shot")
    shot_result = relationship("ShotResult", back_populates="session_shot")
