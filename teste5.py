from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome()

driver.get('https://www.invertexto.com/calculadora-porcentagem')

calculadora1 = driver.find_element_by_xpath("//input[@id='c1v1']")
calculadora1.send_keys("30")
