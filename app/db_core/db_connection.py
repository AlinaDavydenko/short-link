from sqlalchemy import create_engine


class Connection:
    sqlite_database = "sqlite:///db_link.db"

    @staticmethod
    def get_engine():
        """Create connection to db"""
        # create engine 
        engine = create_engine(Connection.sqlite_database)
        return engine 
