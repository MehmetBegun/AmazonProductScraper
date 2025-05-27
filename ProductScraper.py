from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

CSV_FILE = "product.csv"
TARGET_URL = "https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68/"
HEADLESS_OPTION = "--headless=new"
ID_TITLE = "title"
CLASS_PRICE_SELECTOR = ".a-price.a-text-price span.a-offscreen"
DESCRIPTION_LIST_SELECTOR = "ul.a-unordered-list.a-vertical.a-spacing-mini"
ID_RATING = "acrPopover"
ID_IMAGE_WRAPPER = "imgTagWrapperId"

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(HEADLESS_OPTION)
    driver = webdriver.Chrome(
        options=options, service=Service(ChromeDriverManager().install())
    )
    return driver

def scrape_product_data(driver, url):
    driver.get(url)
    product_name = driver.find_element(By.ID, ID_TITLE).text
    price_element = driver.execute_script(
        f'return document.querySelector("{CLASS_PRICE_SELECTOR}")'
    )
    price = driver.execute_script("return arguments[0].textContent", price_element)
    description_list = driver.find_element(By.CSS_SELECTOR, DESCRIPTION_LIST_SELECTOR)
    description_data = [
        item.find_element(By.TAG_NAME, "span").text.strip()
        for item in description_list.find_elements(By.TAG_NAME, "li")
    ]
    rating = driver.find_element(By.ID, ID_RATING).text
    image_element = driver.find_element(By.ID, ID_IMAGE_WRAPPER)
    product_image_url = image_element.find_element(By.TAG_NAME, "img").get_attribute("src")

    return {
        "Name": product_name,
        "Price": price,
        "Description": description_data,
        "Rating": rating,
        "Featured Image": product_image_url
    }

def write_to_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

driver = create_driver()
try:
    product_data = scrape_product_data(driver, TARGET_URL)
    for key, value in product_data.items():
        print(f"{key} : {value}")
    write_to_csv(CSV_FILE, product_data)
    print("Scraping completed and data written to CSV")
finally:
    driver.quit()