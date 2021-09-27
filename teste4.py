from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://selenium.dunossauro.live/todo_list.html')

tarefas = ["Testar OS 100", "Testar OS 101",
           "Testar OS 102", "Testar OS 103", "Testar OS 104"]

descricoes = ["Testar a OS de acordo com especificações.", "Testar a OS printando todas as evidências.", "Testar a OS de acordo com esperado.", "Testar a OS de acordo.", "Testar a OS de acordo com as especificações esperadas."]

tarefa = driver.find_element_by_xpath("//input[@id='todo-name']")
tarefa.send_keys(tarefas[0])

descricao = driver.find_element_by_id("todo-desc")
descricao.send_keys(descricoes[0])

fila = driver.find_element_by_xpath("//button[@id='todo-submit']")
fila.click()

time.sleep(3)

tarefa = driver.find_element_by_xpath("//input[@id='todo-name']")
tarefa.send_keys(tarefas[1])

descricao = driver.find_element_by_id("todo-desc")
descricao.send_keys(descricoes[1])

fila = driver.find_element_by_xpath("//button[@id='todo-submit']")
fila.click()

time.sleep(3)

tarefa = driver.find_element_by_xpath("//input[@id='todo-name']")
tarefa.send_keys(tarefas[2])

descricao = driver.find_element_by_id("todo-desc")
descricao.send_keys(descricoes[2])

fila = driver.find_element_by_xpath("//button[@id='todo-submit']")
fila.click()

time.sleep(3)

tarefa = driver.find_element_by_xpath("//input[@id='todo-name']")
tarefa.send_keys(tarefas[3])

descricao = driver.find_element_by_id("todo-desc")
descricao.send_keys(descricoes[3])

fila = driver.find_element_by_xpath("//button[@id='todo-submit']")
fila.click()

time.sleep(3)

tarefa = driver.find_element_by_xpath("//input[@id='todo-name']")
tarefa.send_keys(tarefas[4])

descricao = driver.find_element_by_id("todo-desc")
descricao.send_keys(descricoes[4])

fila = driver.find_element_by_xpath("//button[@id='todo-submit']")
fila.click()

time.sleep(10)