import pytest
from pylidator import Validator, Validations


def test_validator_contains_data():
    data = {'name': 'Jhon Doe', 'age': 25}
    validation = Validator(data, {})

    assert validation.data == data


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'role': 'admin'
        }, {
            'role': [Validations.ALPHA]
        }, False),
        ({
            'role': 'admin!'
        }, {
            'role': [Validations.ALPHA]
        }, True),
    ]
)
def test_alpha(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'user': 'admin123'
        }, {
            'user': [Validations.ALPHA_NUMERIC]
        }, False),
        ({
            'user': 'admin 123'
        }, {
            'user': [Validations.ALPHA_NUMERIC]
        }, True),
    ]
)
def test_alpha_numeric(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'role': 'admin.user|admin!guest'
        }, {
            'role': [Validations.ALPHA_NUMERIC_PUNCT]
        }, False),
        ({
            'role': 'admin user guest'
        }, {
            'role': [Validations.ALPHA_NUMERIC_PUNCT]
        }, True),
    ]
)
def test_alpha_numeric_punct(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'email': 'valid.email@email.com'
        }, {
            'email': [Validations.EMAIL]
        }, False),
        ({
            'email': 'invalid email'
        }, {
            'email': [Validations.EMAIL]
        }, True),
    ]
)
def test_email(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'name': 'Jhon'
        }, {
            'name': [Validations.MAX(5)]
        }, False),
        ({
            'name': 'Jhon Doe'
        }, {
            'name': [Validations.MAX(5)]
        }, True),
    ]
)
def test_max(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'name': 'Jhon Doe'
        }, {
            'name': [Validations.MIN(4)]
        }, False),
        ({
            'name': 'JD'
        }, {
            'name': [Validations.MIN(4)]
        }, True),
    ]
)
def test_min(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected


@pytest.mark.parametrize(
    "data, rules, expected", [
        ({
            'name': 'Jhon Doe',
            'username': 'j.d'
        }, {
            'username': [Validations.REQUIRED]
        }, False),
        ({
            'name': 'Jhon Doe'
        }, {
            'username': [Validations.REQUIRED]
        }, True),
    ]
)
def test_required(data, rules, expected):
    validation = Validator(data, rules).has_errors
    assert validation == expected
