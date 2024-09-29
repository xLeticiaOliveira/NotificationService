# This class intends to implement a comportament of a database, if necessary.
from datetime import datetime, timedelta

class UsersEmailData:
    def __init__(self) -> None:
        self.users_email_data: dict = {}

    def add_user_email_sent(self, user_id: str, email_type_name: str, sent_at: datetime):
        if user_id not in self.users_email_data:
            self.users_email_data[user_id] = {}
        
        if email_type_name not in self.users_email_data[user_id]:
            self.users_email_data[user_id][email_type_name] = []

        self.users_email_data[user_id][email_type_name].append(sent_at)

    def get_email_amount_in_past_minutes(self, user_id: str, email_type_name: str, minutes: int):
        time_threshold = datetime.now() - timedelta(minutes=minutes)
        return sum(1 for dt in self.users_email_data[user_id][email_type_name] if dt >= time_threshold)