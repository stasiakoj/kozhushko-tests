from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:

    def __init__(self) -> None:
        # Створення обʼєкту для керування браузером
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    def close(self):
        # Закриваємо браузер
        self.driver.close()
