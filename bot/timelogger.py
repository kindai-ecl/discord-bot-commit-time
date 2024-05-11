from datetime import datetime, timedelta
from db.settings import session
from db.schema import User, TimeLog


# ユーザーの合計時間を取得する
def total_time(user_id: int):
    user = session.query(User).filter(User.user_id == user_id).first()
    return user.total_time

# ユーザーの時間ログを追加する
def stamp_time_log(user_id: int, timestamp: datetime, status: str):
    time_log = TimeLog(user_id=user_id, timestamp=timestamp, status=status)
    session.add(time_log)
    session.commit()

# ユーザーの合計時間を計算する
def update_total_time(user_id: int):
    end = session.query(TimeLog).filter(TimeLog.user_id == user_id, TimeLog.status == "end").order_by(TimeLog.timestamp).first()
    start = session.query(TimeLog).filter(TimeLog.user_id == user_id, TimeLog.status == "start").order_by(TimeLog.timestamp).first()
    total_time = end.timestamp - start.timestamp
    return total_time
