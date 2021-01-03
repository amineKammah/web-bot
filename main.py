from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains

captcha_to_text = {
    "9oADAMBAAIRAxEAPwD3+gAoAKAKFlrWmald3dpZ3sM1zZuY7iJW+aNvcf16VvVwtalCM6kWlLVPuJST0RfrAZS1PV9O0a1NzqV5Dawj+KVsfl61tQw1XES5KUXJ+Qm0tzA0j4haJ4h1kabory3rgbpJViZUjHqSQK9DEZNicLR9tiFy9ldXZCqKTsiXxl41s": "USN8",
    "9oADAMBAAIRAxEAPwD3+gAoAKAEZ1QZZgo9ScU0m9gIUvbWSTy0uYWf+6sgJ": "7FKT",
    "9oADAMBAAIRAxEAPwD3+gAoAKAEd1jRndgqqMlicAD1ppNuyA8rvfjno9rqlxDDpt3d2MLbBdw42ue5GccV9TS4UxE6UZSmoyfRmDrpM7vwv4lt": "5UFH",
    "9oADAMBAAIRAxEAPwD3+gCrqWoQaTpd1qF0xWC2iaaQjrtUZOPfitaFGVerGlDeTSXzE3ZXZ85sPGPxm1W8lglSHTrY5WGSUrDFnO1cAfM5x1x+QxX6Mv7PyClFSV5y621ff0Xl+Zye": "9GNN",
    "9oADAMBAAIRAxEAPwD3+gAoAKAOPv8A4peDNMvriyu9aVLi3kaOVBbyttYHBGQpHWvYo5BmNaCqQp3TV1qtvmzN1YJ2bJ9I+I3hTXL6Oz0": "EFU2",
    "9oADAMBAAIRAxEAPwD3+gAoAKACgBk0qQQSTSttjjUsx9AOTVRi5SUVuwOfsfH3hPUDiDX7ANnAWWZYyfwbFehVyjHUvipS+Sv+RCqRfU34biG4QPBLHKhGQyMGB": "RCVC",
    "9oADAMBAAIRAxEAPwD3+gAoAKACgDK8S6udA8OX+qiMSm1iMgQnAY+ma6sDhvrOIhRvbmdiZPlVyn4K8SP4s8MW+ryW4t2lZgYwc4wcf": "UH9G",
    "9oADAMBAAIRAxEAPwD3LV9RTSNFvtTkQulpbyTsgOCwVS2PxxW2GouvWhRWnM0vvdhN2VzxWf4+atMkk9j4ahW3jI3vJK8gXPTJAAFfbQ4QoRajUrO78kv1ZzfWH0R6d4A8Xt418NDVHs": "BWSJ",
    "9oADAMBAAIRAxEAPwD3+gAoAKAMHxp4hfwr4Sv9ZjhSaS3VdkbvtBLMFH884747V35Zg1jcXDDt2T": "MRRP",
    "9oADAMBAAIRAxEAPwD3+gAoAKAILq9tbGMSXdzDbxk4DSyBBn6mrp0p1HaEW35aibS3Ftru2vYvNtbiKeP+": "DBPR",
            }


def buddy_bonus(link, username, password):
    mobile_emulation = {"deviceName": "iPhone X"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(link)
        time.sleep(4)

        print('Clicking on 10$ button')
        bonus_button_xpath = '//*[starts-with(@id, am-modal-container)]/div/div[2]/div/div/div/div/div[1]/div/div/div[4]/div[2]'
        bonus_button = driver.find_element_by_xpath(bonus_button_xpath)
        bonus_button.click()
        time.sleep(5)

        print("writing username")
        username_xpath = '// *[ @ id = "fm-login-id"]'
        driver.find_element_by_xpath(username_xpath).send_keys(username)

        print("writing password")
        password_xpath = '//*[@id="fm-login-password"]'
        driver.find_element_by_xpath(password_xpath).send_keys(password)

        print('clicking on log in button')
        login_button_xpath = '//*[@id="root"]/div[2]/div/div/button'
        driver.find_element_by_xpath(login_button_xpath).click()

        time.sleep(7)

        print('dealing with slider')
        slider_xtext = '//*[@id="nc_1_n1z"]'
        slider = driver.find_element_by_xpath(slider_xtext)

        if slider:
            slide_field_xtext = '//*[@id="nc_1__scale_text"]/span'
            field = driver.find_element_by_xpath(slide_field_xtext)

            offset = field.size["width"]
            move = ActionChains(driver)
            move.drag_and_drop_by_offset(slider, offset - 20, 0).perform()

        time.sleep(5)

        captcha_xpath = '//*[@id="nc_1__imgCaptcha_img"]/img'
        captcha_img = driver.find_element_by_xpath(captcha_xpath)
        print('deqling with captcha')
        if captcha_img:
            captcha_src = captcha_img.get_attribute('src').split("/")[11]

            if captcha_src not in captcha_to_text:
                print(captcha_src)
                raise Exception("Unable to resolve captcha")

            captcha_text = captcha_to_text[captcha_src]

            captcha_input_xpath = '//*[@id="nc_1_captcha_input"]'
            driver.find_element_by_xpath(captcha_input_xpath).send_keys(captcha_text + Keys.RETURN)

        time.sleep(3)

        print('clicking on log in button')
        driver.find_element_by_xpath(login_button_xpath).click()

        time.sleep(7)

        print('claiming bonus\n\n')

        bonus_button = driver.find_elements_by_xpath(bonus_button_xpath)
        if bonus_button:
            bonus_button[0].click()
        else:
            open_button_xpath = '//*[@id="root"]/div/div/div[2]/div[4]/span'
            bonus_button = driver.find_element_by_xpath(open_button_xpath)
            bonus_button.click()

        time.sleep(10)

    except Exception as e:
        print('exception occured')
        print(e)
        driver.quit()
        raise e


if __name__ == '__main__':
    link = 'https://sale.aliexpress.com/__mobile/daily_cash_out_m.htm?invitationCode=cVpVTEo1bllIdW9laGEyVkxNbms2V001UnhJelJOY3VzaC9Cd1N2emdpM1dIZUxWV3YydHExT0s1MU1hdTAyWg&srcSns=sns_Copy&spreaderGameInstanceId=NTJUZDFIT2t4WEppbjhWaGdRVzY2dUVxT25FMmZUQjNncjIzdVpEWjdxcXBJcmo4M1NOU2VVV3FvRUtNZFF5Yg&spreadType=globalshare&bizType=dailycash&spreadCode=cVpVTEo1bllIdW9laGEyVkxNbms2V001UnhJelJOY3VzaC9Cd1N2emdpM1dIZUxWV3YydHExT0s1MU1hdTAyWg&_addShare=no&tt=MG&aff_platform=default&sk=_mrosntv&mergeHashcode=21776565449&description=Your+bonus+is+waiting+to+be+activated.&aff_trace_key=f360efa302b849929ffc1f319946207d-1609454928312-05580-_mrosntv&businessType=dailycash&title=GETUS+%2420.00%21+%23AliExpressbonus+%23BonusBuddies&platform=AE&terminal_id=54da58a5440d48009a2fcd4f95515c45&templateKey=daily_cash_template_global_101_v1'
    username, password = sys.argv[1].split(',')
    buddy_bonus(link, username, password)

