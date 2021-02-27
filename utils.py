from selenium import webdriver

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


def get_boost_link():
    link = "https://sale.aliexpress.com/fr/__mobile/daily_cash_out_m.htm?invitationCode=QnZoMVpqa2J1VFhwbVVBWGtFdkJZckJlM0xFUWtITHlsQW5UQ1JmZ1E2YkduUkF1SGQvWWVsT0s1MU1hdTAyWg&srcSns=sns_Copy&spreaderGameInstanceId=RUhLcVZCMVNBL1FpTUowWkV1L0l1cGVETlpsSzVvT21QdThPZzFKRnRyVzd0NnB0L09jRUI0VjBiampMWEU4eQ&spreadType=promotionGlobalShare&bizType=dailycash&social_params=20077072680&spreadCode=QnZoMVpqa2J1VFhwbVVBWGtFdkJZckJlM0xFUWtITHlsQW5UQ1JmZ1E2YkduUkF1SGQvWWVsT0s1MU1hdTAyWg&_addShare=no&tt=MG&aff_fsk=_mP73L79&aff_platform=default&sk=_mP73L79&aff_trace_key=af1137df475344c781eace691e81f8bc-1614003485880-06131-_mP73L79&shareId=20077072680&businessType=dailycash&platform=AE&terminal_id=cf3553537dfb41b7bae5dd60c0270621"
    return link


def get_driver(proxy=None):
    if proxy:
        webdriver.DesiredCapabilities.FIREFOX["proxy"] = {
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "proxyType": "MANUAL",
        }

    # user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override", user_agent)

    profile.update_preferences()

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("-private")
    firefox_options.add_argument("--headless")
    firefox_options.set_capability("deviceName", "iPhone")
    driver = webdriver.Firefox(
        profile,
        options=firefox_options,
    )
    return driver


def set_location_cookie(driver):
    driver.delete_all_cookies()
