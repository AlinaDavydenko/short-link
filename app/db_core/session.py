from sqlalchemy.orm import sessionmaker
from app.db_core.db_connection import Connection

engine = Connection.get_engine()
SessionLocal = sessionmaker(bind=engine)


def get_session():
    """Get database session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
