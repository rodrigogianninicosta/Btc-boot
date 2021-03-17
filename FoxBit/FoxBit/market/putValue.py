from start.first import *
from market.myMoney import *

def inputerBuy(): 
    finish = driver.find_element_by_xpath("//input[3][@type='text']").send_keys(setMoney.money.replace('.',','))
    finish = driver.find_element(By.XPATH, "//div[@class='summary-wrap']")
    #time.sleep(0.3)
    #setMyBtc(finish.text[41:52].replace(' ',''))
    print('Dinheiro gasto: ' + setMoney.money)

def inputerSell(): 
    #finish = driver.find_element_by_xpath("//input[2][@type='text']").clear()
    #finish = driver.find_element_by_xpath("//input[2][@type='text']").send_keys(setMyBtc.btc)
    #finish = driver.find_element(By.XPATH, "//div[@class='summary-wrap']")
    finish = driver.find_element_by_xpath("//input[3][@type='text']").send_keys(setMoney.money.replace('.',','))
    finish = driver.find_element(By.XPATH, "//div[@class='summary-wrap']")
    #time.sleep(0.3)
    #setMoney(finish.text[38:52].replace(' ',''))
    print('Dinheiro arrecadado: ' + setMoney.money)