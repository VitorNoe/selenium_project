import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class FormyFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        self.driver.get("https://formy-project.herokuapp.com/form")
        self.wait = WebDriverWait(self.driver, 15)
        self.test_data = {
            'first_name': 'Alan',
            'last_name': 'Turing',
            'job_title': 'Software Engineer',
            'education': 'College',
            'sex': 'Male',
            'experience': ['5-9', '10+'],
            'automation_tool': 'Selenium WebDriver',
            'languages': ['Java', 'Python'],
            'continent': 'Europe',
            'date': '2024-12-31'
        }
        
    def tearDown(self):
        self.driver.quit()

    def test_full_form_submission(self):
        print("\nTC-005 - Formulário Completo - Início:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        
        # Preencher campos básicos
        self.driver.find_element(By.ID, "first-name").send_keys(self.test_data['first_name'])
        self.driver.find_element(By.ID, "last-name").send_keys(self.test_data['last_name'])
        self.driver.find_element(By.ID, "job-title").send_keys(self.test_data['job_title'])
        
        # Educação (radio buttons)
        education_value = {'High School': 'hs', 'College': 'college', 'Grad School': 'grad'}
        self.driver.find_element(By.XPATH, 
            f"//input[@name='education'][@value='{education_value[self.test_data['education']]}']").click()
        
        # Sexo (radio buttons)
        self.driver.find_element(By.XPATH,
            f"//input[@name='sex'][@value='{self.test_data['sex']}']").click()
        
        # Experiência (checkboxes)
        for exp in self.test_data['experience']:
            self.driver.find_element(By.XPATH,
                f"//input[@name='exp'][@value='{exp}']").click()
        
        # Ferramenta de automação (dropdown)
        Select(self.driver.find_element(By.ID, "select-tool")).select_by_visible_text(
            self.test_data['automation_tool'])
        
        # Linguagens (multi-select)
        lang_select = Select(self.driver.find_element(By.ID, "select-languages"))
        lang_select.deselect_all()
        for lang in self.test_data['languages']:
            lang_select.select_by_visible_text(lang)
        
        # Continente (dropdown)
        Select(self.driver.find_element(By.ID, "select-continent")).select_by_visible_text(
            self.test_data['continent'])
        
        # Data
        self.driver.find_element(By.ID, "datepicker").send_keys(self.test_data['date'])
        
        # Submissão
        self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary").click()
        
        # Validação
        alert = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        self.assertIn("The form was successfully submitted!", alert.text)
        
        print(f"TC-005 - Dados Submetidos:\n{self.test_data}")
        print("TC-005 - Resultado: Passou - Fim:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

if __name__ == "__main__":
    unittest.main()