from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://vives.icex.es/es/es/icex---home/icex-practicas.html"

options = webdriver.firefox.options.Options()
options.unhandled_prompt_behavior = "accept"

driver = webdriver.Firefox(options=options)
driver.get(url)
cookies_accept = driver.find_element(By.ID, "btn-cookies-accept")
cookies_accept.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h6.fs-4.fw-bold")))
print("hasjdfhasjdhf")

container = driver.find_element(By.ID, "cards-practices")
offers = container.find_elements(By.CSS_SELECTOR, "div.col-12")

dict = {}
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
    print("ID: ", id)
    print("Title: ", title)
    print("Company: ", company)
    print("Location: ", location)
    print("Duration: ", duration)
    print("Start date: ", start_date)
    print("Description: ", description)
    dict[id] = {
        "title": title,
        "company": company,
        "location": location,
        "duration": duration,
        "start date": start_date,
        "description": description
    }
    print("")
