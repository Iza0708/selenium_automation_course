from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

MENU = (By.CSS_SELECTOR, 'div.bm-burger-button')
ABOUT = (By.ID, 'about_sidebar_link')
ABOUT_TEXT=(By.XPATH,'//div[@class="MuiBox-root css-mntjpt"]')
LOGOUT_MENU=(By.ID, 'logout_sidebar_link')
RESET_APP=(By.ID, "reset_sidebar_link")

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.implicitly_wait(5)
wait = WebDriverWait(browser, 10)

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

""""
def test_auth_negative():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('problem_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.XPATH, '//h3[@data-test="error"]')
"""
# Добавление товара в корзину через каталог
def test_auth_add_product_to_cart_from_catalog():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()


#         Удаление товара из корзины через корзину
def test_auth_remove_product_from_cart():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
    remove_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    remove_button.click()

def test_auth_add_product_to_cart_from_product_page():
    login()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
    remove_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    remove_button.click()
    backpack_card = browser.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']")
    backpack_card.click()
    add = browser.find_element(By.XPATH,"//*[@id='inventory_item_container']/div/div/div/button")
    add.click()

def login():
    browser.get('https://www.saucedemo.com/v1/')
    browser.implicitly_wait(10)
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_auth_add_from_card():
    login()
    product_card = browser.find_element(By.XPATH,'//*[@id="item_4_img_link"]/img').click()

"""
def placing_order()
    login()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
"""

# Фильтр
#
# Проверка работоспособности фильтра (A to Z)
# Проверка работоспособности фильтра (Z to A)
# Проверка работоспособности фильтра (low to high)
# Проверка работоспособности фильтра (high to low)

def test_auth_sorted_prices():
    login()
    sorted_prices_1=browser.find_element(By.XPATH, '//option[@value="az"]').click()
    sorted_prices_2=browser.find_element(By.XPATH, '//option[@value="za"]').click()
    sorted_prices_3=browser.find_element(By.XPATH, '//select[@class="product_sort_container"]/option[@value="lohi"]').click()
    sorted_prices_4=browser.find_element(By.XPATH,'//select[@class="product_sort_container"]/option[@value="hilo"]').click()

# Бургер меню
#
# Выход из системы
# Проверка работоспособности кнопки "About" в меню
# Проверка работоспособности кнопки "Reset App State"


def auth_burger_menu():
    login()

    wait.until(EC.element_to_be_clickable(MENU)).click()


def test_about():
    login()
    auth_burger_menu()
    wait.until(EC.element_to_be_clickable(ABOUT)).click()
    search_text=wait.until(EC.visibility_of_element_located(ABOUT_TEXT)).text
    assert 'Web' in search_text


def test_logout_menu():
    login()
    auth_burger_menu()
    wait.until(EC.element_to_be_clickable(LOGOUT_MENU)).click()
    logout_window=browser.current_url
    assert logout_window =='https://www.saucedemo.com/v1/index.html'


def test_reset_app():
    login()
    auth_burger_menu()
    reset_app=wait.until(EC.visibility_of_element_located(RESET_APP)).text
    assert reset_app == 'Reset App State'










    # about_button=browser.find_element(By.XPATH, '//input[@data-test="login-button"]')
    # about_button.click()

#reset_button=browser.find_element(By.XPATH,'//a[@id="reset_sidebar_link"]').click()
#logout_button=browser.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()




