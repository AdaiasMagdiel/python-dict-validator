# Python Dict Validator

A simple dict validator for python projects based in [CodeIgniter's Validator](https://codeigniter4.github.io/userguide/libraries/validation.html).

## Overview

- [Installation](#installation)
- [Usage](#usage)

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

First, you need to import the Validator and Validations classes from pylidator. The Validator class is responsible for the validation, and Validations contains the possible validations.

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

Now, you can pass the dictionary with the data and the dictionary with the rules to the Validator class.

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

To check if the data is valid or invalid, you can check the has_errors attribute of the Validator instance. The has_errors is a boolean attribute that returns True if data is invalid and False otherwise.

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

To get the data from the Validator instance, you can use the ```data``` attribute.

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

### The currents validations from Validations classe are:

| Rules | Parameter | Description |
| --- | --- | --- |
| Email | No | Check if the value of a field is a valid email. |
| Min | Yes | Verify if the value length is longer than the parameter value. |
| Required | No | A generic rule that validates if the field is present in the dictionary. |
