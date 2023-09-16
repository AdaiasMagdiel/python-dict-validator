from pylidator import Validator, Validations

data = {'name': 'John Doe', 'email': 'invalid email.com', 'password': 'error'}

rules = {
    'name': [Validations.MIN(6)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}

validation = Validator(data, rules)
if validation.has_errors:
    print('errors:')
    print(validation.errors)
else:
    print(validation.data)
