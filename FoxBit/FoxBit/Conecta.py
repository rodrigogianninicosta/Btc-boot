from start.login import *
from start.first import *

from market.putValue import *
from market.myMoney import *
from market.myBTC import *
from market.buy import *
from market.sell import *


def getVendaCompra(tipo): 
    # 3 = compra; 4 = venda
    time.sleep(0.7)
    sell = driver.find_element(By.XPATH, '//div[' + tipo + '][@class="last-price"]')
    value = ""
    for i in sell.text:
        if i.isdigit():
            value += i
    return value

def start():
    operation = 'buy'
    con = 60
    setBtc("")
    setMoney("38")
    
    while True:

        time.sleep(0.1)
        if driver.current_url == 'https://app.foxbit.com.br/login':
            login()
            time.sleep(5)

        else:   

            if setBtc.btc == "" or int(setBtc.btc) > int(getVendaCompra('4')) and con >= 0:
                setBtc(getVendaCompra('4'))
                print('\nValor guardado: ' + setBtc.btc + '\n')
                if con <= 10: con = 60

            if con >= 0:
                print(str(con) + 's para efetuar a compra')
                con = con-1
                time.sleep(0.5)

            elif operation == 'buy' and int(getVendaCompra('4')) <= int(setBtc.btc):
                startBuy(getVendaCompra('4'))
                operation = 'sell'      

            elif operation == 'sell' and int(getVendaCompra('3')) > (int(setBtc.btc) + 500000):
                startSell(getVendaCompra('3'))
                operation = 'buy'
                con = 60
                setBtc("")

start()