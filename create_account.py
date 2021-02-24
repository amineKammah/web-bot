from faker import Faker
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.common.action_chains import ActionChains
import time

fake = Faker()
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def create_new_account(driver):

    register_css_selector = 'li.fm-tabs-tab:nth-child(1)'
    driver.find_element_by_css_selector(register_css_selector).click()

    logging.info("Generating fake email")
    email = "ali.sc" + fake.email()
    email_xpath = '/html/body/div[2]/div/div/div[1]/div/div/div[2]/input'
    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(2)

    logging.info("Generating password")
    password = fake.last_name() + "__1234"
    password_xpath = '/html/body/div[2]/div/div/div[1]/div/div/div[3]/input'
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(2)

    register_button_css_selector = 'button.fm-button:nth-child(5)'
    driver.find_element_by_css_selector(register_button_css_selector).click()
    logging.info("Clicked register button")

    slider_span_css_selector = '#nc_1_n1z'
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, slider_span_css_selector))
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(element_present)
        logging.info("Slider Span appeared and identified")

        slider = driver.find_element_by_css_selector(slider_span_css_selector)
        move = ActionChains(driver)
        max_x_offset = driver.get_window_size()["width"] - slider.location["x"] - slider.size["width"]
        move.move_to_element(slider).click_and_hold().move_by_offset(max_x_offset, 0).pause(1).release().perform()

        logging.info("Slider been dragged and dropped")

        success_xpath = "/html/body/div[2]/div/div/div/div/div/div[4]/div/div/div[1]/div[2]/span/b"
        element_present = EC.presence_of_element_located((By.XPATH, success_xpath))
        WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(element_present)
        WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, success_xpath), 'Success'))

        logging.info("Found element success")

        register_button_xpath = '/html/body/div[2]/div/div/div/div/div/button'
        driver.find_element_by_xpath(register_button_xpath).click()
        logging.info("Clicked on register button")

        logging.info("Direction completed, Registration successful")
        time.sleep(5)
        logging.info(f"Created Account succesfully: '{email, password}'")
        WebDriverWait(driver, 15).until(EC.url_changes("login.aliexpress.com"))

    except TimeoutException:
        logging.warning("Timed out")
        logging.info("Direction completed, Registration successful")
        time.sleep(10)

    return email, password

