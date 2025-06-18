# SQLite connection & table creation
"""
db/database.py
------------------
This module sets up the SQLite database using SQLAlchemy.
It defines the voice sample table schema and utility functions for CRUD operations.
"""

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# SQLite database path
DB_PATH = os.path.join(os.getcwd(), "vocalai.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Voice sample Table
class VoiceSample(Base):
    __tablename__ = "voice_samples"
    __table_args__ = {'extend_existing': True}  # Add this line
    voice_name = Column(String,primary_key=True,index=True)
    file_path = Column(String,nullable=False)
  
    # create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)

    # save voice sample
def save_voice_sample(voice_name:str,file_path:str):
        db = SessionLocal()
        try:
            sample = VoiceSample(voice_name=voice_name,file_path=file_path)
            db.merge(sample)  # Use merge to handle updates
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    # Retrieve voice sample by name 
def get_voice_sample(voice_name:str):
        session = SessionLocal()
        result = session.query(VoiceSample).filter(VoiceSample.voice_name == voice_name).first()
        session.close()
        return result

def get_all_voice_names():
    session = SessionLocal()
    try:
        names = session.query(VoiceSample.voice_name).all()
        return [name[0] for name in names]
    finally:
        session.close()
