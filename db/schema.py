from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime

from .settings import Engine
from .settings import Base
from sqlalchemy.orm import relationship

## init database tables

class User(Base):

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    name = Column('name', String(200))
    total_min = Column('total_time', Integer, default=0)  # total time in minutes

    TimeLog = relationship('TimeLog', backref='users')



class TimeLog(Base):

    __tablename__ = 'time_logs'
    __table_args__ = {
        'comment': 'ユーザーの時間ログ'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, 
                    ForeignKey('users.user_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, index=True)
    timestamp = Column('timestamp', DateTime)
    status = Column('status', String(20))  # start or end


Base.metadata.create_all(bind=Engine)