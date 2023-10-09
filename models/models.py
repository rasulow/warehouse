from sqlalchemy import *
from datetime import datetime
from sqlalchemy.orm import relationship
from core import Base


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
