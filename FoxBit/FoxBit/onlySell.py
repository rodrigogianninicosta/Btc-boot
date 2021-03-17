from start.login import *
from start.first import *

from market.putValue import *
from market.myMoney import *
from market.myBTC import *
from market.buy import *
from market.sell import *


def getVendaCompra(tipo): 
    # 3 = compra; 4 = venda
    time.sleep(0.6)
    sell = driver.find_element(By.XPATH, '//div[' + tipo + '][@class="last-price"]')
    value = ""
    for i in sell.text:
        if i.isdigit():
            value += i
    return value

def selling():
    setBtc("27800000")
    setMoney("29")
    
    while True:

        time.sleep(0.1)
        if driver.current_url == 'https://app.foxbit.com.br/login':
            login()
            time.sleep(5)

        else:   
    
            if int(getVendaCompra('3')) >= (int(setBtc.btc)):
                clickSell()
                startSell(getVendaCompra('3'))
                break;

selling()

