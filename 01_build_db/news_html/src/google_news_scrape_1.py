#==============#
#== Jorge Gomez
#== Editado: 3/04/2024

# importo los modulos
from selenium import webdriver
import pandas as pd

#setup webdriver

driver = webdriver.Chrome()

# URL que voy a scrapear

url = 'https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSUwyMHZNRFZxYUdjU0JtVnpMVFF4T1JvQ1EwOG9BQVAB?hl=es-419&gl=CO&ceid=CO%3Aes-419'

driver.get(url)

articulos = driver.find_elements('xpath', '//a[@tabindex="0"]')

len(articulos)

news_links = []

for a_tag in articulos:
    
    print(a_tag.get_attribute('href'), a_tag.text)
    
    new_url = a_tag.get_attribute('href')
    
    driver.execute_script("window.open('');")
    driver.switch_to(driver.current_window_handles[1])
    
    driver.get(new_url)
    link = driver.current_url
    news_links.append(link)
    
    driver.close() 
    driver.switch_to.window(driver.window_handles[0]) 
    
    


    

driver.quit()