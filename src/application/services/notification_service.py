from abc import ABC, abstractmethod
from datetime import datetime

from src.application.services.exceptions.notification_service_exceptions import (
    EmailLimitReachedException,
)
from src.domain.email_type import EmailType
from src.infrastructure.adapters.gateway import Gateway
from src.infrastructure.adapters.local_user_data import UsersEmailData


class NotificationService(ABC):
    @abstractmethod
    def send(self, email_type: EmailType, user_id: str, message: str) -> None:
        pass


class NotificationServiceImpl(NotificationService):
    def __init__(self, gateway: Gateway, users_email_data: UsersEmailData) -> None:
        self.gateway = gateway
        self.users_email_data = users_email_data

    def _verify_rate_limit(self, email_type: EmailType, user_id: str) -> None:
        current_email_amount = self.users_email_data.get_email_amount_in_past_minutes(
            user_id,
            email_type.name,
            email_type.interval_in_minutes,
        )
        if (current_email_amount + 1) > email_type.rate_limit:
            raise EmailLimitReachedException(
                f"Can't send email. Limit of {email_type.rate_limit} emails reached.",
            )

    def send(self, email_type: EmailType, user_id: str, message: str) -> None:
        self._verify_rate_limit(email_type, user_id)
        self.gateway.send(user_id, message)
        self.users_email_data.add_user_email_sent(
            user_id,
            email_type.name,
            datetime.now(),
        )
