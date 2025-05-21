from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class AngleLine(Base):
    __tablename__ = "AngleLine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    angle_id = Column(Integer, ForeignKey("Angle.id"), nullable=False)
    line_id1 = Column(Integer, ForeignKey("JointLine.id"), nullable=False)
    line_id2 = Column(Integer, ForeignKey("JointLine.id"), nullable=False)


    angle = relationship("Angle", back_populates="angleLines")

    jointLine_line1 = relationship(
        "JointLine",
        foreign_keys=[line_id1],
        back_populates="angleLine_as_line1"
    )
    jointLine_line2 = relationship(
        "JointLine",
        foreign_keys=[line_id2],
        back_populates="angleLine_as_line2"
    )
