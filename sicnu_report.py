# -*- coding: utf-8 -*-

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def main(userName, passWord, login_url):
    mobileEmulation = {'deviceName': 'iPhone 4'}
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument('disable-dev-shm-usage')
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    driver.set_window_size(320, 680)
    try:
        driver.get(login_url)
        username = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, 'mobileUsername'))
        )
        password = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, 'mobilePassword'))
        )
        username.send_keys(userName)
        password.send_keys(passWord)
        login_button = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, 'load'))
        )
        login_button.click()
        logging.info(f'{userName}-signed in')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div'))
        )
        logging.info(f'{userName}-contents loaded')
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="mint-indicator" and @style="display: none;"]'))
        )
        logging.info(f'{userName}-mint-indicator disappear')
        add_button = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button'))
        )
        logging.info(f'{userName}-add_button loaded')
        add_button.click()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="mint-indicator" and @style="display: none;"]'))
        )
        logging.info(f'{userName}-mint-indicator disappear')
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        logging.info(f'{userName}-js executed')
        tijiao = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/button'))
        )
        tijiao.click()
        queding = WebDriverWait(driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[3]/button[2]'))
        )
        queding.click()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="cjataj7ar"]'))
        )
        logging.info(f'{userName}-succeed')
        driver.save_screenshot(f'{datetime.datetime.now():%Y-%m-%d}-{userName}.png')
    except Exception as e:
        logging.warning(f'{userName}-{e}')
    finally:  
        driver.close()
        driver.quit()


if __name__ == "__main__":
    undergraduate = 'http://ehall.sicnu.edu.cn/qljfw/sys/lwReportEpidemicUndergraduate/*default/index.do' # 本科
    postGraduate = 'http://ehall.sicnu.edu.cn/qljfw/sys/lwReportEpidemicPostGraduate/*default/index.do' # 研究生
    userInfo = [
        ["2020******", "*******", undergraduate],
        ['2020******', '*******', postGraduate]
    ]
    for h in userInfo:
        main(*h)
