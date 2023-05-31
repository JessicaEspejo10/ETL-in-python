# Import the objects needed
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

# Initialize the base and set inheritance
Base = declarative_base()

class PprRawAll(Base):
    # Set the table name
    __tablename__ = "ppr_raw_all"
    # Create a primary key integer column id
    id = Column(Integer, primary_key=True)
    date_of_sale=Column(DateTime)
    address=Column(String)
    postal_code=Column(String)
    country=Column(String)
    price=Column(Integer)
    description=Column(String)