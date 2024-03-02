import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DriverError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


load_dotenv()
DRIVER_PATH = os.environ.get("DRIVER_PATH")
if DRIVER_PATH is None:
    raise DriverError("Driver Path is NULL")
service = Service(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://www.bestbuy.com/?intl=nosplash")

time.sleep(3)
search_bar = driver.find_element(By.CSS_SELECTOR, ".search-input")
search_bar.send_keys("samsung")
search_bar.submit()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "[data-track='Category - Show More']").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[text()="Cell Phones"]').click()
time.sleep(4)
driver.find_element(By.XPATH, '//a[text()="Samsung"]').click()
time.sleep(4)
sort_dropdown = driver.find_element(
    By.ID,
    "sort-by-select",
)

select_sort = Select(sort_dropdown)
select_sort.select_by_visible_text("Price High to Low")

time.sleep(5)

link = driver.find_element(
    By.CSS_SELECTOR,
    ".sku-item-list li:first-child .sku-title > a",
)

print(link.text)

time.sleep(5)
