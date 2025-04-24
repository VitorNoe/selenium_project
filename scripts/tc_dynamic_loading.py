import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

class DynamicLoadingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        self.driver.implicitly_wait(0)  # Desativa waits implícitos
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        
    def tearDown(self):
        self.driver.quit()

    def test_hello_world_displayed(self):
        print("\nTC-003 - Carregamento Dinâmico - Início:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        # Aguarda botão Start
        try:
            start_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Start')]"))
            )
        except TimeoutException:
            self.fail("Botão Start não encontrado em 10 segundos")

        # Início do teste
        start_time = datetime.now()
        start_btn.click()
        
        # Aguarda texto Hello World!
        try:
            hello_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
            )
            tempo_espera = (datetime.now() - start_time).total_seconds()
            
            self.assertEqual(hello_element.text, "Hello World!")
            print(f"TC-003 - Tempo de carregamento: {tempo_espera:.2f}s - Passou - Fim:", 
                  datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        except TimeoutException:
            print(f"TC-003 - Timeout após 10s - Falhou - Fim:", 
                  datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            self.fail("Texto não apareceu dentro do timeout")

if __name__ == "__main__":
    unittest.main()