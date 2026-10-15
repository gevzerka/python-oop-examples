import re

class Customer:
    def __init__(self, name, email):
        self.name = self._validate_name(name)
        self.email = self._validate_email(email)

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or len(name.strip()) < 1:
            raise ValueError("Имя должно быть строкой длиной не менее одного символа")
        return name.strip()
    @staticmethod
    def _validate_email(email):
        if not isinstance(email, str):
            raise ValueError("Указана неверная почта")
        else:
            match = re.fullmatch(r'\w+@\w+\.\w+', email.strip())
            if not match:
                raise ValueError("Указана неверная почта")
            return match.group().strip()

    def update_email(self, new_email):
        self.email = self._validate_email(new_email)