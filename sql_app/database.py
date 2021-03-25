from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import cloudinary

cloudinary.config(
    cloud_name= "drtasweku",
    api_key= "767344675117213",
    api_secret ="sz7NK9UYS7o35yOBXfL5vAdr9K0"
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgres://audcltysmukkjt:fa3bf618e3522f1adea51b8ae6ca778c3fdd2e70b9a2f68defcd7e588cf0a024@ec2-52-71-161-140.compute-1.amazonaws.com:5432/del74sq4ertbru"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()