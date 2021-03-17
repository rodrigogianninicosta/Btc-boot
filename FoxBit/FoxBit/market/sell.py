from start.first import *
from market.myMoney import *
from market.myBTC import *
from market.putValue import *

def startSell(value):
    setMoney(str(float(setMoney.money) + 0.10))
    inputerSell()
    sell()
    print('Vendido por: ' + value)
    clickBuy()

def sell():
    but = driver.find_element(By.XPATH, '//button[@class="btn btn-action"]')
    but.click()

def clickBuy():
    buy = driver.find_element(By.XPATH, "//*[text()='Comprar']")
    buy.click()
