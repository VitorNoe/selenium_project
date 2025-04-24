import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

class SauceDemoTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")
        
    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        print("\nTC-001 - Login válido - Início:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")
        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()
        
        inventory_container = self.driver.find_element(By.ID, "inventory_container")
        self.assertTrue(inventory_container.is_displayed())
        print("TC-001 - Resultado: Passou - Fim:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def test_unsuccessful_login(self):
        print("\nTC-002 - Login inválido - Início:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_btn = self.driver.find_element(By.ID, "login-button")
        
        username.send_keys("invalid_user")
        password.send_keys("wrong_password")
        login_btn.click()
        
        error_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_container.text)
        print("TC-002 - Resultado: Passou - Fim:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

if __name__ == "__main__":
    unittest.main()