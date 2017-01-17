from selenium import webdriver
import time
import csv

key = input('key = ')

first_name = []
last_name = []
title = []
company = []

driver = webdriver.Firefox()
first_url = 'http://s15.a2zinc.net/clients/emeraldexpo/slats2017/Public/e_Login.aspx?FromPage=e_exhibitorconsole'
driver.get(first_url)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_txtPassword']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_txtPassword']").send_keys(key)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_chkSignAuto']").click()
time.sleep(3)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnlogin").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Console_432966']/div/div/div[2]/div[1]/div/div/div/h4/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='attendeeSearchControls']/div[3]/div/ul/li[1]/label/input").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='attendeeSearchControls']/div[3]/div/ul/li[2]/label/input").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='btnSearch']").click()
time.sleep(7)
a = 0
while a<1250:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    a+=1
    print(a)
for f_name in driver.find_elements_by_xpath("//*[@id='attendeeList']/tbody/tr/td[2]//a"):
    print('it work')
    first_name.append(f_name.text)
    print(a)
for l_name in driver.find_elements_by_xpath("//*[@id='attendeeList']/tbody/tr/td[3]//a"):
    print('it work')
    last_name.append(l_name.text)
    print(a)
for dr_title in driver.find_elements_by_xpath("//*[@id='attendeeList']/tbody/tr/td[4]//a"):
    print('it work')
    title.append(dr_title.text)
    print(a)
for dr_company in driver.find_elements_by_xpath("//*[@id='attendeeList']/tbody/tr/td[5]//a"):
    print('it work')
    company.append(dr_company.text)
    print(a)
with open ('ready_new.csv','w',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('first_name', 'last_name', 'title','company'))
    for row in zip(first_name, last_name, title,company):
        writer.writerow(row)
