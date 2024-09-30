class EmailType:
    def __init__(self, name: str, rate_limit: int, interval_in_minutes: int) -> None:
        self.name = name
        self.rate_limit = rate_limit
        self.interval_in_minutes = interval_in_minutes
