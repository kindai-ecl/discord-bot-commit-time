from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .settings import Base, Engine

# init database tables


class User(Base):

    __tablename__ = "users"
    __table_args__ = {"comment": "ユーザー情報のマスターテーブル"}

    user_id = Column("user_id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(200))
    total_min = Column("total_time", Integer, default=0)  # in minutes

    TimeLog = relationship("TimeLog", backref="users")


class TimeLog(Base):

    __tablename__ = "time_logs"
    __table_args__ = {"comment": "ユーザーの時間ログ"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        "user_id",
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    timestamp = Column("timestamp", DateTime)
    status = Column("status", String(20))  # start or end


Base.metadata.create_all(bind=Engine)
