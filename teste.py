from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.4devs.com.br/gerador-de-curriculo')

driver.find_element_by_xpath("//input[@id='name']").send_keys("Luiz Henrique Alberto de Camargo")
driver.find_element_by_xpath("//input[@id='email']").send_keys("luiz.henriquecamargo@hotmail.com")
driver.find_element_by_xpath("//input[@id='nationality']").clear()
driver.find_element_by_xpath("//input[@id='nationality']").send_keys("Brasileiro")
driver.find_element_by_xpath("//input[@id='age']").send_keys("21")

driver.find_element_by_xpath("//select[@id='gender']").send_keys("Masculino")
driver.find_element_by_xpath("//select[@id='marital']").send_keys("Solteiro(a)")

driver.find_element_by_xpath("//input[@id='telephone']").send_keys("(15) 99652-1338")
driver.find_element_by_xpath("//input[@id='mobile']").send_keys("(15) 2107-8933)")
driver.find_element_by_xpath("//input[@id='address']").send_keys("Rua dos Curiós")
driver.find_element_by_xpath("//input[@id='city']").send_keys("Porto Feliz")
driver.find_element_by_xpath("//input[@id='state']").send_keys("São Paulo")
driver.find_element_by_xpath("//input[@id='cep']").send_keys("18540-000")
driver.find_element_by_xpath("//textarea[@id='career-goal']").send_keys("Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! ")

driver.find_element_by_xpath("//input[@id='btnNext']").click()

time.sleep(3)

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "course[0]"))
    )
finally:
    driver.find_element_by_id("course[0]").send_keys("Curso de QA")
    #driver.execute_script("document.getElementById('course[0]').scrollIntoView();")

    driver.find_element_by_id("school[0]").send_keys("Fatec Itu")
    driver.find_element_by_id("school_conclusion_year[0]").send_keys("2018")
    driver.find_element_by_id("other_courses").send_keys("Sem cursos")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='btnNext']").click()

    driver.find_element_by_id("company[0]").send_keys("4R Sistemas")
    driver.find_element_by_id("company_begin[0]").send_keys("2021")
    driver.find_element_by_id("work_present[0]").click()
    driver.find_element_by_id("company_office[0]").send_keys("Estagiário de QA")
    driver.find_element_by_id("company_functions[0]").send_keys("Realizar testes, automação, gerenciamento, etc...")
    driver.find_element_by_id("other_activity").send_keys("Não possuo")
    time.sleep(3)
    driver.find_element_by_id("btnNext").click()

    time.sleep(5)
    driver.find_element_by_id("other_informations").send_keys("Não possuo informações adicionais.")
    driver.find_element_by_id("btnPreview").click()
    time.sleep(10)

