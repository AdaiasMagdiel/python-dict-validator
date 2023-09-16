from typing import Any


class Validations:
    REQUIRED = 'required'
    EMAIL = 'email'

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

    def required(self, key: str, value: str):
        return key in self.data

    def min(self, key: str, value: str):
        if not value.isdigit():
            raise Exception(
                'Min validation requires a number to verify.' +
                f' But has received "{value}" instead'
            )

        item = self.data.get(key)
        return item and len(item) >= int(value)

    def email(self, key: str, value: str):
        cond_1 = '@' in self.data[key]

        item = self.data.get(key)
        return item and '@' in item and '.' in item.split('@')[-1]

    @classmethod
    def _total_rules(cls):
        items = [key for key in cls.__dict__.keys() if not key.startswith('_')]
        return len(items)


class Messages:
    def __init__(self) -> None:
        if Validations._total_rules() != self._total_rules():
            raise Exception(
                'Theres rules in Validations that are not implemented in Rules class'
            )

        self.messages = {
            'required': 'The "{}" is required',
            'min': 'The "{}" must have a {} min length',
            'email': 'The "{}" must be a valid email',
        }

    def required(self, key: str, value: str):
        return self.messages['required'].format(key)

    def min(self, key: str, value: str):
        return self.messages['min'].format(key, value)

    def email(self, key: str, value: str):
        return self.messages['email'].format(key, value)

    @classmethod
    def _total_rules(cls):
        items = [key for key in cls.__dict__.keys() if not key.startswith('_')]
        return len(items)


class Validator:
    errors: dict = {}

    def __init__(
        self, data: dict[str, Any], rules: dict[str, list[str]]
    ) -> None:
        self.rules_class = Rules(data)
        self.messages = Messages()
        self.verify(rules)

    def verify(self, rules: dict[str, list[str]]):
        for field, _rules in rules.items():
            for rule in _rules:
                self.verify_rule(field, rule)

    def verify_rule(self, field: str, rule: str):
        rule, _, value = rule.partition(':')

        rule_attr = getattr(self.rules_class, rule.lower())
        res = rule_attr(field, value)
        if res is False:
            message = getattr(self.messages, rule.lower())

            if field not in self.errors:
                self.errors[field] = []

            self.errors[field].append(message(field, value))

    @property
    def data(self) -> dict:
        return self.rules_class.data

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
