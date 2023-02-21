import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        self.username = "ritter1",
        self.email = "ritter11@gmail.com"
        self.password = "12345"

    # TEST CASE POSITIVE REGRISTER
    def test_register_success(self):
        # Test register data valid
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        name = driver.find_element(By.ID, "name_register")
        name.send_keys(self.username)
        email = driver.find_element(By.ID, "email_register")
        email.send_keys(self.email)
        password = driver.find_element(By.ID, "password_register")
        password.send_keys(self.password)

        btnRegister = driver.find_element(By.ID, "signup_register")
        btnRegister.click()
        time.sleep(3)

        # validasi
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#swal2-title").text
        respons_message = driver.find_element(
            By.CSS_SELECTOR, "#swal2-content").text

        self.assertIn(response_data, 'berhasil')
        self.assertEqual(respons_message, 'created user!')

    def test_register_email(self):
        # Test data register email terdaftar
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        name = driver.find_element(By.ID, "name_register")
        name.send_keys(self.username)
        email = driver.find_element(By.ID, "email_register")
        email.send_keys(self.email)
        password = driver.find_element(By.ID, "password_register")
        password.send_keys(self.password)

        btnRegister = driver.find_element(By.ID, "signup_register")
        btnRegister.click()
        time.sleep(3)

        # validasi
        response_data = driver.find_element(
            By.CSS_SELECTOR, "#swal2-title").text
        respons_message = driver.find_element(
            By.CSS_SELECTOR, "#swal2-content").text

        self.assertIn(response_data, 'Oops...')
        self.assertEqual(respons_message, 'Gagal Register!')

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
