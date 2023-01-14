from allure import epic, feature, title


@epic('Frontend')
@feature('Регистрация пользователей')
class TestRegistration:
    """
    Тесты для проверки регистрации пользователей
    """

    @title('Регистрация пользователя с валидными данными')
    def test_registration_user_with_valid_data(self, registration_page, registration_success_page):
        registration_page.open(path=registration_page.path)
        registration_page.should_be_open_registration_page()

        registration_page.fill_registration_form()
        registration_page.click_on_register_button()

        registration_success_page.should_be_open_registration_success_page()
        registration_success_page.should_be_confirm_register_message()

    @title('Регистрация пользователя с пустыми полями в форме регистрации')
    def test_registration_user_with_empty_field(self, registration_page, data_registration_emptyfields):
        registration_page.open(path=registration_page.path)
        registration_page.should_be_open_registration_page()

        registration_page.fill_registration_form(
            is_random=False,
            gender=data_registration_emptyfields[0],
            firstname=data_registration_emptyfields[1],
            lastname=data_registration_emptyfields[2],
            email=data_registration_emptyfields[3],
            password=data_registration_emptyfields[4],
            confirm_password=data_registration_emptyfields[5],
        )
        registration_page.click_on_register_button()

        registration_page.can_see_error_message_with_text(expected_error_message=data_registration_emptyfields[6])

    @title('Переход на страницу регистрации из хедера')
    def test_go_to_registration_page_from_header(self, main_page, header, registration_page):
        main_page.open()

        header.go_to_register_page()
        registration_page.should_be_open_registration_page()
