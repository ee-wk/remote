from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddContact:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def fill_in_form(self):
        """填写表单信息"""
        self.driver.find_element_by_id("username").send_keys("张三")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("三三")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("66668888")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("02088886666")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("872464959@qq.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("天河区")
        self.driver.find_element_by_id("memberAdd_title").send_keys("员工")

    def test_add_contact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 进入登录页
        with open("data/cookies.yaml", encoding="utf-8") as f:  # 获取cookies
            cookies = yaml.safe_load(f)
        for cookie in cookies:  # 添加cookies
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")  # 进入通讯录页
        # WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')))
        sleep(1)
        # 添加联系人
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.fill_in_form()
        # self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
