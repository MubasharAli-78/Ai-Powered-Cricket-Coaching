from sqlalchemy import Integer, ForeignKey, Column
from sqlalchemy.orm import relationship
from config import Base


class SessionPlayer(Base):
    __tablename__ = "SessionPlayer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('Session.id'), nullable=False)
    player_id = Column(Integer, ForeignKey('User.id'), nullable=False)


    session = relationship("Session", foreign_keys=[session_id], back_populates="session_player")
    player = relationship("User", foreign_keys=[player_id], back_populates="session_Player")
    session_Shot = relationship("SessionShot", back_populates="session_player")


