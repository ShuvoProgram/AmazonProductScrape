from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common import exceptions

path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.amazon.com/')
# full screen
browser.maximize_window()
input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.ID, 'nav-search-submit-button')

input_search.send_keys('laptop')
sleep(1)
search_button.click()

product_class = "a-size-medium"


products = []
for i in range(10):
    try:
        # print('scraping page', i+1)
        product = browser.find_elements(By.CLASS_NAME, product_class)
        # products.extend(product)
        for p in product:
            products.append(p.text)
        next_button = browser.find_element(By.CLASS_NAME, "s-pagination-separator")
        next_button.click()
        sleep(4)
    except exceptions.StaleElementReferenceException as e:
        print(e)

print(len(products))
print(products)
