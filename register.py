import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        # Rubahlah field isi data variable masing-masing dibawah ini, jika ingin test run lagi
        self.username = "SyarifRidho"
        self.email = "syarifridho@gmail.com"
        self.password = "123425"

    # TEST CASE POSITIVE REGISTER

    def test_registered_email(self):
        # Test data register email terdaftarr
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

    # TEST CASE NEGATIVE REGISTER

    def test_blank_name(self):
        # Test data nama kosong
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        name = driver.find_element(By.ID, "name_register")
        name.send_keys("")
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

    def test_blank_password(self):
        # Test data password kosong
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        name = driver.find_element(By.ID, "name_register")
        name.send_keys(self.username)
        email = driver.find_element(By.ID, "email_register")
        email.send_keys(self.email)
        password = driver.find_element(By.ID, "password_register")
        password.send_keys("")

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

    def test_all_blank(self):
        # Test data all blank
        driver = self.browser
        driver.get("http://barru.pythonanywhere.com/daftar")
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        name = driver.find_element(By.ID, "name_register")
        name.send_keys("")
        email = driver.find_element(By.ID, "email_register")
        email.send_keys("")
        password = driver.find_element(By.ID, "password_register")
        password.send_keys("")

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
