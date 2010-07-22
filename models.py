from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

#metadata.create_all(engine)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Song(Base):
    __tablename__ = 'songs'
    
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    path = Column(String)

    def __init__(self, path):
        self.count = 0
        self.path = path

    def __repr__(self):
        return "<Song('%s', '%s')>" % (self.path, self.count)

    def update_count(self):
        self.count = self.count + 1
