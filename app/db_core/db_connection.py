from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sqlite_database = "sqlite:///db_link.db"

# create engine 
engine = create_engine(sqlite_database)

# create class session 
Session = sessionmaker(autoflush=False, bind=engine)
