from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class TeamPlayer(Base):
    __tablename__ = "TeamPlayer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    player_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    team = relationship("Team", back_populates="team_Player")
    user = relationship("User", back_populates="team_Player")
