from typing import Dict

from src.application.services.notification_service import NotificationServiceImpl
from src.domain.email_type import EmailType
from src.infrastructure.adapters.gateway import Gateway
from src.infrastructure.adapters.local_user_data import UsersEmailData


def create_email_types() -> Dict[str, EmailType]:
    return {
        "news": EmailType("news", 1, 1440),
        "status": EmailType("status", 2, 1),
        "marketing": EmailType("marketing", 3, 60),
        "update": EmailType("update", 2, 60),
    }


if __name__ == "__main__":
    print("Initializing..")
    service = NotificationServiceImpl(Gateway(), UsersEmailData())
    email_types = create_email_types()

    service.send(email_types["news"], "user", "news 1")
    service.send(email_types["news"], "user2", "news 2")
    service.send(email_types["update"], "user", "update 1")
    service.send(email_types["news"], "user", "news 3")
