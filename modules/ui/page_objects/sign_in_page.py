from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        # Відкриваємо сторінку https://github.com/login
        self.driver.get(SignInPage.URL)
    
    def try_login(self, username, password):
        # Знаходимо поле, в яке будемо вводити неправильне імʼя користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильно імʼя користувача або поштову аодресу
        login_elem.send_keys(username)

        # Знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # Вводимо неправильний пароль
        pass_elem.send_keys(password)

        # Знаходимо кнопку sign_in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Емулюємо клік лівою кнопкою мишки
        btn_elem.click()

    def check_title(self, expected_title):
        # Перевіримо, що назва сторінки така, яку ми очікуємо
        return self.driver.title == expected_title
