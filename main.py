from create_account import *
import threading
from utils import set_location_cookie, get_driver
from proxy import fill_proxies_queue, get_proxy
import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def create_accounts():
    while True:
        logging.info("Getting proxy")
        proxy = get_proxy()
        logging.info(f"Got proxy, {proxy}")
        for _ in range(10):
            try:
                driver = get_driver(proxy)
                register_link = "https://login.aliexpress.com/"
                driver.get(register_link)
                set_location_cookie(driver)
                email, password = create_new_account(driver)

                with open("accounts.txt", "a") as myfile:
                    myfile.write(f"{email}:{password}\n")

                driver.close()
            except Exception as e:
                logging.warning(e)
                break


for _ in range(5):
    threading.Thread(target=create_accounts).start()

fill_proxies_queue(1_000)
