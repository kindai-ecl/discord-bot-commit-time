from datetime import datetime, timedelta

from sqlalchemy import desc
from db.settings import session
from db.schema import User, TimeLog

# ユーザーを追加する
def register_user(user_id: int, name: str):
    user = User(user_id=user_id, name=name)
    session.add(user)
    session.commit()

# ユーザーが存在するか確認する
def authorized(user_id: int):
    user = session.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return False
    return True

# ユーザーの合計時間を取得する
def total_time(user_id: int):
    user = session.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return "ありません。登録が必要です。\n/register コマンドで登録してください"
    min = user.total_min % 60
    hour = user.total_min // 60
    return f"{hour}時間{min}分です"

# ユーザーの時間ログを追加する
def stamp_time_log(user_id: int, timestamp: datetime, status: str):
    time_log = TimeLog(user_id=user_id, timestamp=timestamp, status=status)
    session.add(time_log)
    session.commit()

# ユーザーの合計時間を計算する
def update_total_time(user_id: int):
    end = session.query(TimeLog).filter(TimeLog.user_id == user_id, TimeLog.status == "end").order_by(desc(TimeLog.timestamp)).first()
    start = session.query(TimeLog).filter(TimeLog.user_id == user_id, TimeLog.status == "start").order_by(desc(TimeLog.timestamp)).first()
    total_time = end.timestamp - start.timestamp
    commit_time = total_time // timedelta(minutes=1)

    user = session.query(User).filter(User.user_id == user_id).first()
    user.total_min += commit_time
    session.commit()
    return 
