from start.first import *
from start.keys import *


def login():
    user()
    password()
    open()
    

def user():
    email = driver.find_element(By.XPATH, '//input[@id="email"]')
    email.send_keys(use)

def password():
    passwor = driver.find_element(By.XPATH, '//input[@id="password"]')
    passwor.send_keys(number)

#Abrir página de compra e venda
def open():
    time.sleep(1)
    button = driver.find_element(By.XPATH, '//button[@id="submit"]')
    button.click()
    time.sleep(5)
    print('Entrando na sua conta e abrindo a página...')
    driver.execute_script('window.location.href = "https://app.foxbit.com.br/trade.html"')