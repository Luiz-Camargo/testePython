from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random

driver = webdriver.Chrome()
driver.get('https://www.4devs.com.br/gerador_de_pessoas')

sexo = driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]")
sexo.click()

idade = driver.find_element_by_xpath("//select[@id='idade']")
idade.send_keys("18")

estado = driver.find_element_by_xpath("//select[@id='cep_estado']")
estado.send_keys("SP")

cidade = driver.find_element_by_xpath("//select[@id='cep_cidade']")
cidade.send_keys("Porto Feliz")

gerar = driver.find_element_by_xpath("//input[@id='bt_gerar_pessoa']")
gerar.click()
time.sleep(1)
gerar.click()
time.sleep(1)
gerar.click()
time.sleep(1)
gerar.click()
time.sleep(1)