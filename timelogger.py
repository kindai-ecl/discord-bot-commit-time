from db.settings import session
from db.schema import User, TimeLog
from datetime import datetime, timedelta

def total_time(user_id: int):
    # ユーザーの合計時間を取得する
    user = session.query(User).filter(User.user_id == user_id).first()
    return user.total_time

def add_time_log(user_id: int, start_time: datetime, end_time: datetime):
    # ユーザーの時間ログを追加する
    time_log = TimeLog(user_id=user_id, start_time=start_time, end_time=end_time)
    session.add(time_log)
    session.commit()

def calc_total_time(user_id: int, start_time: datetime, end_time: datetime):
    # ユーザーの合計時間を計算する
    time_logs = session.query(TimeLog).filter(TimeLog.user_id == user_id).all()
    total_time = timedelta()
    for time_log in time_logs:
        total_time += time_log.end_time - time_log.start_time
    return total_time