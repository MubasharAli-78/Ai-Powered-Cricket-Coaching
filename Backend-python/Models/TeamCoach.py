from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class TeamCoach(Base):
    __tablename__ = "TeamCoach"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    coach_id = Column(Integer, ForeignKey('User.id'), nullable=False)


    team = relationship("Team", back_populates="team_Coach")
    user = relationship("User", back_populates="team_Coach")
