from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def get_cookies():
    option = Options()
    option.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=option)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    expect = expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="menu_index"]/span'))
    WebDriverWait(driver, 30).until(expect)
    cookies = driver.get_cookies()
    with open("./data/cookies.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookies, f)
    # driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
    # sleep(2)
    # driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()


if __name__ == '__main__':
    get_cookies()
