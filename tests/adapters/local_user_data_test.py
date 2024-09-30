from datetime import datetime

from src.infrastructure.adapters.local_user_data import UsersEmailData
from tests.conftest import BaseConfTest


class TestLocalUserData(BaseConfTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        super().setUp()
        self.adapter = UsersEmailData()

    def test_add_user_email_sent(self) -> None:
        datetime_now = datetime.now()
        self.assertIsNone(
            self.adapter.add_user_email_sent("user", "name", datetime_now),
        )
        self.assertEqual(
            self.adapter.users_email_data,
            {"user": {"name": [datetime_now]}},
        )

    def test_get_email_amount_in_past_minutes_inexistant(self) -> None:
        self.assertEqual(
            self.adapter.get_email_amount_in_past_minutes("new user", "new type", 10),
            0,
        )

    def test_get_email_amount_in_past_minutes_existant(self) -> None:
        self.adapter.users_email_data = {"user": {"type": [datetime.now()]}}
        self.assertEqual(
            self.adapter.get_email_amount_in_past_minutes("user", "type", 10),
            1,
        )
