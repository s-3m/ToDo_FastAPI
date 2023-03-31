from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    is_finished = Column(Boolean, default=False, server_default=expression.false())
    created = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates='tasks')
