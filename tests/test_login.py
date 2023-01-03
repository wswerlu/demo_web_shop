from allure import epic, feature, title


@epic('Frontend')
@feature('Авторизация пользователей')
class TestLogin:
    """
    Тесты для проверки авторизации пользователей
    """

    @title('Авторизация пользователя с валидными данными')
    def test_login_user_with_valid_data(self, main_page, header, login_page, create_user):
        main_page.open()
        main_page.should_be_open_main_page()

        header.go_to_login_page()
        login_page.should_be_open_login_page()

        login_page.fill_login_form(
            email=create_user['email'],
            password=create_user['password'],
        )
        login_page.click_on_login_button()

        header.can_see_user_email(email=create_user['email'])
