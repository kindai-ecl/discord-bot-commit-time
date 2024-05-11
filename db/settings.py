import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import event

# DBの接続
DATABASE = 'sqlite:///../db/timelog.db'

Engine = create_engine(
    DATABASE,
    echo=True
)
Base = declarative_base()

session = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

Base = declarative_base()
Base.query = session.query_property()

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()