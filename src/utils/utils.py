from datetime import datetime


class Utils:
    @staticmethod
    def validate_date(date_str: str) -> bool:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def user_key(name: str, birth_date: str) -> str:
        return f"{name}_{birth_date}"
