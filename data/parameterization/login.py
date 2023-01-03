invaliddata = [
    ['wrong@email.ru', None, 'No customer account found', 'Login with wrong email'],
    [None, 'wrong_password', 'The credentials provided are incorrect', 'Login with wrong password'],
    ['wrong@email.ru', 'wrong_password', 'No customer account found', 'Login with wrong email and password'],
]  # данные для теста test_login_user_with_invalid_data
