from allure import epic, feature, title


@epic('Frontend')
@feature('Регистрация пользователей')
class TestRegistration:
    """
    Тесты для проверки регистрации пользователей
    """

    @title('Регистрация пользователя с валидными данными')
    def test_registration_user_with_valid_data(self, main_page, header, registration_page, registration_success_page):
        main_page.open()
        main_page.should_be_open_main_page()

        header.go_to_register_page()
        registration_page.should_be_open_registration_page()

        registration_page.fill_registration_form()
        registration_page.click_on_register_button()

        registration_success_page.should_be_open_registration_success_page()
        registration_success_page.should_be_confirm_register_message()
