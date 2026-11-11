import re

_ENAIL_RE= re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = self._validate_name(value)

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = self._validate_email(value)

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        return name.strip()

    @staticmethod
    def _validate_email(email: str) -> str:
        if not isinstance(email, str) or not _ENAIL_RE.fullmatch(email.strip()):
            raise ValueError("Указана неверная почта")
        return email.strip()

    def __repr__(self) -> str:
        return f"Customer(name={self._name!r}, email={self._email!r}"