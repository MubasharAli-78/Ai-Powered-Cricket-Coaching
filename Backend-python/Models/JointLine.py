from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class JointLine(Base):
    __tablename__ = 'JointLine'

    id = Column(Integer, primary_key=True, autoincrement=True)
    line_name = Column(String(30))
    joint_id1 = Column(Integer, ForeignKey('Joint.id'), nullable=False)
    joint_id2 = Column(Integer, ForeignKey('Joint.id'), nullable=False)


    joint1 = relationship("Joint", foreign_keys=[joint_id1], back_populates="jointLine_joint1")
    joint2 = relationship("Joint", foreign_keys=[joint_id2], back_populates="jointLine_joint2")

    angleLine_as_line1 = relationship(
        'AngleLine',
        foreign_keys="AngleLine.line_id1",
        back_populates='jointLine_line1'
    )
    angleLine_as_line2 = relationship(
        'AngleLine',
        foreign_keys="AngleLine.line_id2",
        back_populates='jointLine_line2'
    )
