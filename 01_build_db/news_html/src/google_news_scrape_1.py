#==============#
#== Jorge Gomez
#== Editado: 29/03/2024

# importo los modulos
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time 
#setup webdriver

driver = webdriver.Chrome()

# URL que voy a scrapear

url = 'https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRFZxYUdjU0JtVnpMVFF4T1JvQ1EwOG9BQVAB?hl=es-419&gl=CO&ceid=CO%3Aes-419'

driver.get(url)
wait = WebDriverWait(driver, 10)
time.sleep(3)

articulos = driver.find_elements('xpath', '//a[@tabindex="0"]')
len(articulos)

news_links = []

for i in range(len(articulos)):
    new_url = articulos[i].get_attribute('href') 
    print(new_url)
    
    driver.execute_script("window.open('');")
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1]) 
    driver.get(new_url)
    
    time.sleep(1)
    
    link = driver.current_url
    news_links.append(link)
    print(len(news_links))
    
    driver.close() 
    driver.switch_to.window(driver.window_handles[0]) 
   
driver.quit()

