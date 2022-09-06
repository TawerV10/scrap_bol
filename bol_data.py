from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

options = webdriver.ChromeOptions()

options.add_argument(f'user-agent={UserAgent().random}')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe' # Chrome location

path = r'C:\Users\name\Documents\GitHub\chromedriver.exe' # driver location
service = Service(path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.bol.com/")

print("Press a key from the below list to select the category: ")

print("Press 1 for Boeken")
print("Press 2 for Elektronica")
print("Press 3 for Speelgoed")
print("Press 4 for Wonen")
print("Press 5 for Baby")
print("Press 6 for Koken & Tafelen")
print("Press 7 for Elektronica")
print("Press 8 for Beauty")

print("Press 9 for Sport")
print("Press 10 for Films & Series")
print("Press 11 for Computer")
print("Press 12 for Klussen")
print("Press 13 for Muziek")
print("Press 14 for Damesmode")
print("Press 15 for Herenmode")
print("Press 16 for Kindermode")
print("Press 17 for Games")
print("Press 18 for Persoonlijke verzorging")
print("Press 19 for Tuin")
print("Press 20 for Huishouden")
print("Press 21 for Dieren")
print("Press 22 for Kantoor & School")
print("Press 23 for Gezondheid")
print("Press 24 for Kamperen & Outdoor")
print("Press 25 for Erotiek")
print("Press 26 for Reisbagage & Reisaccessoires")
print("Press 27 for Auto & Motor")
print("Press 28 for AEten & Drinken")

value = int(input())

if (value == 1):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[0].click()

elif (value == 2):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[1].click()

elif (value == 3):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[2].click()

elif (value == 4):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[3].click()

elif (value == 5):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[4].click()

elif (value == 6):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[5].click()

elif (value == 7):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[6].click()

elif (value == 8):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[7].click()

elif (value == 9):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[8].click()

elif (value == 10):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[9].click()

elif (value == 11):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[10].click()

elif (value == 12):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[11].click()

elif (value == 13):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[12].click()

elif (value == 14):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[13].click()

elif (value == 15):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[14].click()

elif (value == 16):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[15].click()

elif (value == 17):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[16].click()

elif (value == 18):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[17].click()

elif (value == 19):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[18].click()

elif (value == 20):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[19].click()

elif (value == 21):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[20].click()

elif (value == 22):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[21].click()

elif (value == 23):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[22].click()

elif (value == 24):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[23].click()

elif (value == 25):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[24].click()

elif (value == 26):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[25].click()

elif (value == 27):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[26].click()

elif (value == 28):
    driver.find_elements(By.XPATH, "//a[@class='image-card__image-link']")[27].click()

else:
    print("Error")

first_page = driver.current_url

Title = []
Link = []

pages = input("How many pages do you want to run?: ")

count = 1
for i in range(1, int(pages) + 1):

    url = f"{first_page}?page={i}&sort=bestverkocht_11&view=list"

    driver.get(url)
    sleep(3)

    items = len(driver.find_elements(By.CLASS_NAME, "product-item--row"))

    for i in range(0, items):
        Title.append(driver.find_elements(By.XPATH, "//a[@data-test='product-title']")[i].get_attribute('href'))
        Link.append(driver.find_elements(By.XPATH, "//a[@data-test='product-title']")[i].text)

        print(count)
        count += 1

Records = []
for i in range(len(Title)):
    Records.append((Title[i], Link[i]))

file = pd.DataFrame(Records, columns=["Product Name", "Link"])
file.to_csv('output.csv', index=False, encoding='utf-8')
