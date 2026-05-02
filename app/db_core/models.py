from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    original_url = Column(String(200), unique=True, nullable=False)
    short_code = Column(String(50), unique=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
