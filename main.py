from pylidator import Validator, Validations

user_01 = {
    'name': 'John Doe',
    'username': 'jhon.doe',
    'email': 'jhon.doe@email.com',
    'password': 'notsegurepassword'
}
user_02 = {
    'name': 'Link',
    'username': 'hyruleshero',
    'email': 'not valid email',
    'password': '123'
}

rules = {
    'name': [Validations.MIN(6)],
    'username': [Validations.MIN(3)],
    'email': [Validations.EMAIL],
    'password': [Validations.MIN(6)],
}

validation = Validator(user_01, rules)
print(validation.has_errors)  # False

validation = Validator(user_02, rules)
print(validation.has_errors)  # True
