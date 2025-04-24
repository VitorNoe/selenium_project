import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random

class DemoBlazePurchaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.wait = WebDriverWait(self.driver, 15)
        self.test_data = {
            'name': f"User_{random.randint(100,999)}",
            'country': "Testland",
            'city': "Silicon Valley",
            'card': f"4111{random.randint(100000000000, 999999999999)}",
            'month': "12",
            'year': "2025"
        }
        
    def tearDown(self):
        self.driver.quit()

    def test_complete_purchase(self):
        print("\nTC-004 - Fluxo de Compra - Início:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        # Seleciona primeiro produto
        product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tbodyid']/div[1]/div/div/h4/a")))
        product.click()
        
        # Adiciona ao carrinho
        add_to_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add to cart')]")))
        add_to_cart.click()
        
        # Lida com alerta
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        
        # Acessa carrinho
        cart_link = self.wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        cart_link.click()
        
        # Inicia pedido
        place_order = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
        place_order.click()
        
        # Preenche formulário
        form_fields = {
            'name': self.driver.find_element(By.ID, "name"),
            'country': self.driver.find_element(By.ID, "country"),
            'city': self.driver.find_element(By.ID, "city"),
            'card': self.driver.find_element(By.ID, "card"),
            'month': self.driver.find_element(By.ID, "month"),
            'year': self.driver.find_element(By.ID, "year")
        }
        
        for field, element in form_fields.items():
            element.send_keys(self.test_data[field])
        
        # Finaliza compra
        purchase_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]")
        purchase_btn.click()
        
        # Captura confirmação
        confirmation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert")))
        confirmation_text = confirmation.text
        print(f"\nDados da Compra:\n{confirmation_text}")
        
        self.assertIn("Thank you for your purchase!", confirmation_text)
        print("TC-004 - Resultado: Passou - Fim:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

if __name__ == "__main__":
    unittest.main()