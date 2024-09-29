from infrastructure.adapters.gateway import Gateway
from application.services.notification_service import NotificationServiceImpl
from typing import Dict
from domain.email_type import EmailType

def create_email_types() -> Dict[str, EmailType]:
    return {
        "news": EmailType("news", 1, 1440),
        "status": EmailType("status", 2, 1),
        "marketing": EmailType("marketing", 3, 60),
        "update": EmailType("update", 2, 60)
    }

if __name__ == "__main__":
    service = NotificationServiceImpl(Gateway())
    email_types = create_email_types()

    service.send(email_types["news"], "user", "news 1")
    service.send(email_types["news"], "user", "news 2")
    service.send(email_types["news"], "user", "news 3")
    service.send(email_types["news"], "another user", "news 1")
    service.send(email_types["update"], "user", "update 1")