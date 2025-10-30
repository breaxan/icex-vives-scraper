import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://vives.icex.es/es/es/icex---home/icex-practicas.html"

driver = webdriver.Firefox()
driver.get(url)

# Accept cookies
cookies_accept = driver.find_element(By.CSS_SELECTOR, "#btn-cookies-accept")
cookies_accept.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h6.fs-4.fw-bold")))

pages = driver.find_elements(By.CSS_SELECTOR, "a.page-link")[1:26]

dict = {}
for page in pages:
    page.click()
    time.sleep(3)
    container = driver.find_element(By.CSS_SELECTOR, "#cards-practices")
    offers = container.find_elements(By.CSS_SELECTOR, "div.col-12")
    for offer in offers:
        txt = offer.find_element(By.CSS_SELECTOR, "h6.fs-4.fw-bold").text
        id = txt[:4]
        title = txt[6:]
        info = offer.find_elements(By.CSS_SELECTOR, "div.d-flex.mb-2 > *")
        company = info[0].text
        location = info[1].text[11:]
        duration = info[2].text[21:]
        start_date = info[3].text[17:]
        description = offer.find_element(By.CSS_SELECTOR, "p.fs-6").text
        link = "https://vives.icex.es/content/icexvives/es/es/icex---home/icex-practicas/icex-practicas-detalles.html?c=P" + id
        print("ID: " + id)
        print("Title: " + title)
        print("Company: " + company)
        print("Location: " + location)
        print("Duration: " + duration)
        print("Start date: " + start_date)
        print("Description: " + description)
        print("Link: " + link)
        print("")
        dict[id] = {
            "title": title,
            "company": company,
            "location": location,
            "duration": duration,
            "start date": start_date,
            "description": description,
            "link": link
        }
driver.close()

df = pd.DataFrame.from_dict(dict, orient="index")
df.to_excel("data.xlsx")