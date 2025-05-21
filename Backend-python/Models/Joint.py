from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from config import Base


class Joint(Base):
    __tablename__ = 'Joint'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))


    jointLine_joint1 = relationship("JointLine", foreign_keys="JointLine.joint_id1", back_populates="joint1")
    jointLine_joint2 = relationship("JointLine", foreign_keys="JointLine.joint_id2", back_populates="joint2")
