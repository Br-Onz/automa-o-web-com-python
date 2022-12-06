from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')  # ignora certificate errors
options.add_argument('start-maximized')  # inicia o navegador maximized
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # Não aparece um pop-up
driver = webdriver.Chrome(options=options)
driver.get("https://github.com/")  # link
element = WebDriverWait(driver, 30).until(  # Vai ficar procurando a tag por 30 segundos
    expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]')  # XPATH da tag
    )
)
element.send_keys("Br-ONZ")
element = WebDriverWait(driver, 30).until(  # Vai ficar procurando a tag por 30 segundos
    expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '//*[@id="jump-to-suggestion-search-global"]')  # XPATH da tag
    )
)
element = driver.find_element(
    By.XPATH, '//*[@id="jump-to-suggestion-search-global"]')  # XPATH da tag
element.click()  # click na tag
sleep(1)
element = WebDriverWait(driver, 30).until(  # Vai ficar procurando a tag por 30 segundos
    expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/div[1]/div[4]/main/div/div[2]/nav[1]/a[10]')  # XPATH da tag
    )
)
element = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[4]/main/div/div[2]/nav[1]/a[10]')  # XPATH da tag
element.click()  # click na tag
sleep(1)

element = WebDriverWait(driver, 30).until(  # Vai ficar procurando a tag por 30 segundos
    expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '//*[@id="user_search_results"]/div/div/div[2]/div[1]/div[1]/a[1]')  # XPATH da tag
    )
)
element = driver.find_element(
    By.XPATH, '//*[@id="user_search_results"]/div/div/div[2]/div[1]/div[1]/a[1]')  # XPATH da tag
element.click()  # click na tag
sleep(300)
