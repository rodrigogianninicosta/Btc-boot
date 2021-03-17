from start.first import *
from market.myBTC import *
from market.putValue import *

def startBuy(value):
    inputerBuy()
    buy()
    print('Comprado por: ' + value)
    clickSell()

def buy():
    but = driver.find_element(By.XPATH, '//button[@class="btn btn-action"]')
    but.click()

def clickSell():
    sell = driver.find_element(By.XPATH, "//*[text()='Vender']")
    sell.click()


