from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class FriendPhrase(Base):
    __tablename__= 'catchPhrases'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    language = Column(String)
