from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,Integer, String)


def u(text):
    return text.encode("utf-8")


Base = declarative_base()

class ArabIndoDB(Base):
    __tablename__ = "arabindo"

    id = Column(Integer, primary_key=True)
    arab_mushakkal = Column(String)
    arab_bila_tashkeel = Column(String)
    indo = Column(String)

    def __repr__(self):
        return "Arabindo(arab={}, indo={})".format(
        u(self.arab_mushakkal), self.indo
        )
