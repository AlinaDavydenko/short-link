from app.db_core.models import Base
from app.db_core.db_connection import Connection


def init_db():
    engine = Connection.get_engine()
    Base.metadata.create_all(engine)
