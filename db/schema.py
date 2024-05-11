from sqlalchemy import Column, Integer, String, Float, DateTime

from .settings import Engine
from .settings import Base


class User(Base):

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    name = Column('name', String(200))
    total_time = Column('total_time', String)  # string format "H:MM"

class TimeLog(Base):

    __tablename__ = 'time_logs'
    __table_args__ = {
        'comment': 'ユーザーの時間ログ'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    timestamp = Column('timestamp', DateTime)
    status = Column('status', String(20))  # start or end


Base.metadata.create_all(bind=Engine)
print('DBのテーブルを作成しました')