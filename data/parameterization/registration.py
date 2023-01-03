from utils.generated_test_data import UserData

user = UserData()
user_data = {
    'gender': user.gender(),
    'firstname': user.firstname(),
    'lastname': user.lastname(),
    'email': user.email(),
    'password': user.password(),
}

emptyfields = [
    [user_data['gender'], '', user_data['lastname'], user_data['email'], user_data['password'], user_data['password'],
     'First name is required.', 'Empty firstname field'],
    [user_data['gender'], user_data['firstname'], '', user_data['email'], user_data['password'],
     user_data['password'], 'Last name is required.', 'Empty lastname field'],
    [user_data['gender'], user_data['firstname'], user_data['lastname'], '', user_data['password'],
     user_data['password'], 'Email is required.', 'Empty email field'],
    [user_data['gender'], user_data['firstname'], user_data['lastname'], user_data['email'], '', '',
     'Password is required.', 'Empty password and confirm password fields'],
    [user_data['gender'], user_data['firstname'], user_data['lastname'], user_data['email'],
     user_data['password'], '', 'Password is required.', 'Empty confirm password fields'],
]  # данные для теста test_registration_user_with_empty_field
