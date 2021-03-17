from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import asyncio
import os
import time 

os.environ['MOZ_HEADLESS'] = '1'
driver = webdriver.Firefox()
driver.get('https://app.foxbit.com.br/login')


