import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_register_success(self):
        # test
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()

        name = driver.find_element(By.ID, "name_register")
        name.send_keys("vendra122")
        email = driver.find_element(By.ID, "email_register")
        email.send_keys("admin1122223@gmail.com")
        password = driver.find_element(By.ID, "password_register")
        password.send_keys("admin12323245")

        btnRegister = driver.find_element(By.ID, "signup_register")
        btnRegister.click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#swal2-title").text
        respons_message = driver.find_element(
            By.CSS_SELECTOR, "#swal2-title").text

        self.assertIn('berhasil', response_data)
        self.assertIn('berhasil', respons_message)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
