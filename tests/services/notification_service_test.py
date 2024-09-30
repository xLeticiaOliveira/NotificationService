from datetime import datetime

from src.application.services.exceptions.notification_service_exceptions import (
    EmailLimitReachedException,
)
from src.application.services.notification_service import NotificationServiceImpl
from src.domain.email_type import EmailType
from src.infrastructure.adapters.gateway import Gateway
from src.infrastructure.adapters.local_user_data import UsersEmailData
from tests.conftest import BaseConfTest


class TestNotificationService(BaseConfTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    def setUp(self) -> None:
        super().setUp()
        self.service = NotificationServiceImpl(Gateway(), UsersEmailData())

    def test_verify_rate_limit_ok(self):
        self.assertIsNone(
            self.service._verify_rate_limit(EmailType("news", 1, 1440), "user"),
        )
        self.assertIsNone(
            self.service._verify_rate_limit(EmailType("status", 1, 1440), "user"),
        )

    def test_verify_rate_limit_error(self):
        self.service.users_email_data.users_email_data["other user"] = {
            "news": [datetime.now()],
        }
        self.assertRaises(
            EmailLimitReachedException,
            self.service._verify_rate_limit,
            EmailType("news", 1, 1440),
            "other user",
        )

    def test_send_ok(self):
        self.assertIsNone(
            self.service.send(
                EmailType("other news", 1, 1440),
                "other user",
                "message",
            ),
        )

    def test_send_error(self):
        self.assertIsNone(
            self.service.send(
                EmailType("other news error", 1, 1440),
                "other user error",
                "message",
            ),
        )
        self.assertRaises(
            EmailLimitReachedException,
            self.service.send,
            EmailType("other news error", 1, 1440),
            "other user error",
            "message",
        )
