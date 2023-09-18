from typing import Any


class Validations:
    ALPHA = 'alpha'
    EMAIL = 'email'
    REQUIRED = 'required'

    @classmethod
    def MAX(cls, value: int):
        return f'max:{value}'

    @classmethod
    def MIN(cls, value: int):
        return f'min:{value}'

    @classmethod
    def _total_rules(cls):
        items = [key for key in cls.__dict__.keys() if not key.startswith('_')]
        return len(items)


class Rules:
    def __init__(self, data: dict) -> None:
        if Validations._total_rules() != self._total_rules():
            raise Exception(
                'Theres rules in Validations that are not implemented in Rules class'
            )

        self.data = data

    def alpha(self, key: str, value: str):
        item = self.data.get(key)
        return item and item.isalpha()

    def email(self, key: str, value: str):
        item = self.data.get(key)
        return item and '@' in item and '.' in item.split('@')[-1]

    def max(self, key: str, value: str):
        if not value.isdigit():
            raise Exception(
                'Max validation requires a number to verify.' +
                f' But has received "{value}" instead'
            )

        item = self.data.get(key)
        return item and len(item) <= int(value)

    def min(self, key: str, value: str):
        if not value.isdigit():
            raise Exception(
                'Min validation requires a number to verify.' +
                f' But has received "{value}" instead'
            )

        item = self.data.get(key)
        return item and len(item) >= int(value)

    def required(self, key: str, value: str):
        return key in self.data

    @classmethod
    def _total_rules(cls):
        items = [key for key in cls.__dict__.keys() if not key.startswith('_')]
        return len(items)


class Messages:
    messages = {
        'alpha': 'The "{}" must have only alphabetic characters',
        'email': 'The "{}" must be a valid email',
        'max': 'The "{}" must have a {} max length',
        'min': 'The "{}" must have a {} min length',
        'required': 'The "{}" is required',
    }

    def __init__(self) -> None:
        if Validations._total_rules() != len(self.messages):
            raise Exception(
                'Theres rules in Validations that are not messages\n.' +
                f'Validations: {Validations._total_rules()} - ' +
                f'Messages: {len(self.messages)}'
            )


class Validator:
    def __init__(
        self, data: dict[str, Any], rules: dict[str, list[str]]
    ) -> None:
        self.errors = {}
        self.rules_class = Rules(data.copy())
        self.messages = Messages()
        self.verify(rules.copy())

    def verify(self, rules: dict[str, list[str]]):
        for field, _rules in rules.items():
            for rule in _rules:
                self.verify_rule(field, rule)

    def verify_rule(self, field: str, rule: str):
        rule, _, value = rule.partition(':')

        rule_attr = getattr(self.rules_class, rule.lower())
        res = rule_attr(field, value)
        if res is False:
            message = self.messages.messages.get(rule.lower(), '')

            if field not in self.errors:
                self.errors[field] = []

            self.errors[field].append(message.format(field, value))

    @property
    def data(self) -> dict:
        return self.rules_class.data

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
