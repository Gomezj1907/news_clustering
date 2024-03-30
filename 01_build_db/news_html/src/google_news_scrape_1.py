#==============#
#== Jorge Gomez
#== Editado: 29/03/2024

# importo los modulos
from selenium import webdriver
import pandas as pd

#setup webdriver

driver = webdriver.Chrome()

# URL que voy a scrapear

url = 'https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRFZxYUdjU0JtVnpMVFF4T1JvQ1EwOG9BQVAB?hl=es-419&gl=CO&ceid=CO%3Aes-419'

driver.get(url)

articulos = driver.find_elements('xpath', '//a[@tabindex="0"]')

driver.execute_script()

for a_tag in articulos:
    print(a_tag.get_attribute('href'), a_tag.text)
    
    
len(articulos)

driver.quit()