from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.4devs.com.br/gerador-de-curriculo')

nome = driver.find_element_by_xpath("//input[@id='name']")
nome.send_keys("Luiz Henrique Alberto de Camargo")

email = driver.find_element_by_xpath("//input[@id='email']")
email.send_keys("luiz.henriquecamargo@hotmail.com")

driver.find_element_by_xpath("//input[@id='nationality']").clear()

nacionalidade = driver.find_element_by_xpath("//input[@id='nationality']")
nacionalidade.send_keys("Brasileiro")

idade = driver.find_element_by_xpath("//input[@id='age']")
idade.send_keys("21")

genero = driver.find_element_by_xpath("//select[@id='gender']")
genero.send_keys("Masculino")

estadocivil = driver.find_element_by_xpath("//select[@id='marital']")
estadocivil.send_keys("Solteiro(a)")

celular = driver.find_element_by_xpath("//input[@id='telephone']")
celular.send_keys("(15) 99652-1338")

telefone = driver.find_element_by_xpath("//input[@id='mobile']")
telefone.send_keys("(15) 2107-8933)")

rua = driver.find_element_by_xpath("//input[@id='address']")
rua.send_keys("Rua José Elias Habice, nº86")

cidade = driver.find_element_by_xpath("//input[@id='city']")
cidade.send_keys("Porto Feliz")

estado = driver.find_element_by_xpath("//input[@id='state']")
estado.send_keys("São Paulo")

cep = driver.find_element_by_xpath("//input[@id='cep']")
cep.send_keys("18540-000")

descricao = driver.find_element_by_xpath("//textarea[@id='career-goal']")
descricao.send_keys(
    "Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! Eu sou o cara! ")

driver.find_element_by_xpath("//input[@id='btnNext']").click()

time.sleep(3)

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "course[0]"))
    )
finally:
    driver.find_element_by_id("course[0]").send_keys("Curso de QA")
    # driver.execute_script("document.getElementById('course[0]').scrollIntoView();")

    driver.find_element_by_id("school[0]").send_keys("Fatec Itu")
    driver.find_element_by_id("school_conclusion_year[0]").send_keys("2018")
    driver.find_element_by_id("other_courses").send_keys("Sem cursos")
    time.sleep(3)
    driver.find_element_by_xpath("//input[@id='btnNext']").click()

    driver.find_element_by_id("company[0]").send_keys("4R Sistemas")
    driver.find_element_by_id("company_begin[0]").send_keys("2021")
    driver.find_element_by_id("work_present[0]").click()
    driver.find_element_by_id(
        "company_office[0]").send_keys("Estagiário de QA")
    driver.find_element_by_id("company_functions[0]").send_keys(
        "Realizar testes, automação, gerenciamento, etc...")
    driver.find_element_by_id("other_activity").send_keys("Não possuo")
    time.sleep(3)
    driver.find_element_by_id("btnNext").click()

    time.sleep(5)
    driver.find_element_by_id("other_informations").send_keys(
        "Não possuo informações adicionais")
    driver.find_element_by_id("btnPreview").click()
    time.sleep(10)
