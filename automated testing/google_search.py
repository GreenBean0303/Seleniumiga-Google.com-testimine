from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

try:
    #avab Google
    driver.get("https://www.google.com")
    #Leiab otsingu kasti
    search_box = driver.find_element(By.NAME, "q")
    #Sisetab otsingupäringu
    search_query = "Selenium Python"
    search_box.send_keys(search_query)
    #Vajutab ENTER
    search_box.send_keys(Keys.RETURN)
    #Ootab 3 sekundit
    time.sleep(3)
    #Leiab kõik otsingutulemuste pealkirjad
    search_results = driver.find_elements(By.CSS_SELECTOR, "h3")
    #Kontrolli kas tulemused leiti

    if search_results:
        print("\nTop 5 otsingutulemust:")
        for result in search_results[:5]:  # Kuvame ainult esimesed 5
            print("-", result.text)
    else:
        print(" Otsingutulemusi ei leitud!")

finally:
    #suleb akna
    driver.quit()