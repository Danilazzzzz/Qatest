from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'http://192.168.10.107/SuperbasaWWW2/'
driver.get(base_url)
driver.maximize_window()
"""Тест не правильного логина и пароля"""
"""Авторизация"""
login = "R03-BRIG"
passw = "R03-BRIG-05"
user_name = driver.find_element(By.XPATH, "//input[@id='txtUserName']")
user_name.send_keys(login)
password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(passw)
button_ok = driver.find_element(By.XPATH, "//input[@id='butLogIn']")
button_ok.click()
text_1 = driver.find_element(By.XPATH, "//span[@id='lblMessage']")
text_2 = text_1.text                                       
print(text_2)