from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class PastResults(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)

    words = relationship("Word", back_populates="history")


    
class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(255), nullable=False)
    count = Column(Integer, nullable=False)
    history_id = Column(Integer, ForeignKey("history.id"))
    
    history = relationship("PastResults", back_populates="words")


