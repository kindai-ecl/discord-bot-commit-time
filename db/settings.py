import os 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# DBファイルの作成
if not os.path.isfile('timelog.db'):
    with open('timelog.db', 'w'):
        pass
# DBの接続
DATABASE = 'sqlite:///timelog.db'

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