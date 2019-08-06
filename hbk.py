from selenium import webdriver
import os
from driver import *
import unittest
from time import sleep
import logging

def hbk_login(url):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("guangxindaihbk")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("Credit2go")
    driver.find_element_by_id("login-submit").click()
    a = range(2,0,-1)
    b = len(a)
    for i in a:
        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/ul/li[3]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/div[2]/div[2]/ul/li/div/a").click()
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr/td[1]/a").click()
        if i==1:
            urla = '/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/form[2]/div/table/tbody/tr/td[2]/a'
        else:
            urla = '/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/form[2]/div/table/tbody/tr['+str(i)+']/td[2]/a'
        driver.find_element_by_xpath(urla).click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/a[1]").click()
        sleep(2)
        driver.find_element_by_css_selector("[value='5']").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div[7]/form/input[6]").click()
        print('第',i,"已关闭")
        title = '第'+str(i)+"已关闭"
        logging.info(title)
        sleep(2)






if __name__ == "__main__":
    url = "https://jerp2p-ticket.jx-bank.com/login"
    hbk_login(url)

