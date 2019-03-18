from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    brandname = Column(String)

    def __init__(self, brandname):
        self.brandname = brandname

    def __repr__(self):
        return "<Brand('%s')>" % (self.brandname)


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    countryname = Column(String)

    def __init__(self, countryname):
        self.countryname = countryname

    def __repr__(self):
        return "<Country('%S')>" % (self.countryname)


class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    display = Column(Float)
    ram = Column(Integer)
    hdd = Column(Integer)
    price = Column(Integer)
    text = Column(String(255))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    country_id = Column(Integer, ForeignKey('country.id'))
    brand = relationship("Brand", backref="phone")
    country = relationship("Country", backref="phone")
