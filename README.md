# Python Dict Validator

A simple dict validator for python projects based in [CodeIgniter's Validator](https://codeigniter4.github.io/userguide/libraries/validation.html).

## Overview

- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)

## Installation

In progress...

## Usage

Considering the current dictionary, let's see how to validate.

```python
user = {
    'name': 'John Doe',
    'username': 'jhon.doe',
    'email': 'jhon.doe@email.com',
    'password': 'notsegurepassword'
}
```

First, you need to import the `Validator` and `Validations` classes from pylidator. The `Validator` class is responsible for the validation, and `Validations` contains the possible validations.

```python
from pylidator import Validator, Validations
```

Next, you need to create the rules to validate the dictionary.

```python
from pylidator import Validator, Validations

rules = {
    'name': [Validations.MIN(6)],
    'username': [Validations.MIN(3)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}
```

Now, you can pass the dictionary with the data and the dictionary with the rules to the `Validator` class.

```python
from pylidator import Validator, Validations


user = {
    'name': 'John Doe',
    'username': 'jhon.doe',
    'email': 'jhon.doe@email.com',
    'password': 'notsegurepassword'
}

rules = {
    'name': [Validations.MIN(6)],
    'username': [Validations.MIN(3)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}

validation = Validator(user, rules)
```

To check if the data is valid or invalid, you can check the `has_errors` attribute of the `Validator` instance. The `has_errors` is a boolean attribute that returns `True` if data is invalid and `False` otherwise.

```python
from pylidator import Validator, Validations


user = {
    'name': 'John Doe',
    'username': 'jhon.doe',
    'email': 'jhon.doe@email.com',
    'password': 'notsegurepassword'
}

rules = {
    'name': [Validations.MIN(6)],
    'username': [Validations.MIN(3)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}

validation = Validator(user, rules)
print(validation.has_errors)  # False
```

To get the data from the `Validator` instance, you can use the `data` attribute.

```python
from pylidator import Validator, Validations


user = {
    'name': 'John Doe',
    'username': 'jhon.doe',
    'email': 'jhon.doe@email.com',
    'password': 'notsegurepassword'
}

rules = {
    'name': [Validations.MIN(6)],
    'username': [Validations.MIN(3)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}

validation = Validator(user, rules)
print(validation.has_errors)  # False
print(validation.data == user) # True
```

### Validations Rules:

These are the current validations rules that you can use.

| Rules | Parameter | Description |
| --- | --- | --- |
| Email | No | Check if the value of a field is a valid email. |
| Min | Yes | Verify if the value length is longer than the parameter value. |
| Required | No | A generic rule that validates if the field is present in the dictionary. |

## Documentation

- [Validator](#validator)
- [Validations](#validations)

### Validator

The `Validator` class is responsible for data validation based on specific rules.

- `has_errors` (attribute): A boolean that indicates whether there are errors in the validated data. If there are no errors, this attribute will be `False`.
- `data` (attribute): A dictionary containing the unchanged data to be validated.
- `__init__(data: dict[str, Any], rules: dict[str, list[str]])` (method): The constructor of the class that initializes the `Validator` instance. It takes two arguments:
  - `data` (type: dict[str, Any]): The dictionary containing the data to be validated.
  - `rules` (type: dict[str, list[str]]): The dictionary containing the fields of data and a list of validation rules to be applied to the data.

To see how to use, check the [usage](#usage).

### Validations:

- `EMAIL` (attribute): Used to verify if field value are a valid email.
- `REQUIRED` (attribute): Indicates that the fields are required in the data; it is a generic rule that all the other rules use for the verification itself.
- `MIN(value: int)`: Requires a length of at least the specified value.
