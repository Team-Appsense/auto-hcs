print("Auto-HCS V1.0 is now loding...")
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from os import system
import sys
import json
with open("./config.json", "r", encoding="utf-8") as r:
    config = json.load(r)

print("Auto-HCS V1.0 is loded!!")
print("Developed by. leehyowon (Team.Appsense)")

try:
    for i in range(len(config['User'])):
        print('['+str(i)+']'+' '+config['User'][i]["name"])
    #print('[all] 등록된 모든 사람')
    user_number = input("유저 번호를 입력하여주세요 : ")
    if user_number != "all":
        user_number = int(user_number)
    user = config['User'][user_number]
except:
    print("올바른 번호를 입력하여 주세요")
    system('pause')
    sys.exit()

print("[Auto-HCS info] 자가진단을 시작합니다.")
options = webdriver.ChromeOptions()
options.add_argument('window-size=720,1080')
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(10)

driver.get(url='https://hcs.eduro.go.kr/#/loginHome')

#자가진단 버튼
driver.find_element("css selector", "#btnConfirm2").click()

#학교 찾기 버튼
driver.find_element("css selector", "#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button").click()

#시/도 선택
Select(driver.find_element("css selector", "#sidolabel")).select_by_value(config['City'])

#학교급
Select(driver.find_element("css selector", "#crseScCode")).select_by_value(config['Level'])

#학교이름
org_input = driver.find_element("css selector", "#orgname")
org_input.send_keys(config['School'])
org_input.send_keys(Keys.RETURN)

#학교 선택
driver.find_element("css selector", "#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > a").click()
driver.find_element("css selector", "#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input").click()

#이름
driver.find_element("css selector", "#user_name_input").send_keys(user['name'])

#생년월일
driver.find_element("css selector", "#birthday_input").send_keys(user['birthday'])

#비밀번호
driver.find_element("css selector", "#WriteInfoForm > table > tbody > tr:nth-child(4) > td > div > button").click()

key_pad = {}
for i in range(2, 10):
    for elem in driver.find_element("css selector", '#password_mainDiv > div:nth-child('+str(i)+')').find_elements("xpath", ".//*"):
        key_pad[elem.get_attribute("aria-label")] = elem

password = user['password']
for i in range(4):
    key_pad[password[i]].click()

#done
driver.find_element("css selector", '#btnConfirm').click()

#start
try:
    WebDriverWait(driver, 30).until(
        expected_conditions.element_to_be_clickable(("css selector", "#container > div > section.memberWrap > div:nth-child(2) > ul > li > a.survey-button"))
    )
    driver.find_element("css selector", "#container > div > section.memberWrap > div:nth-child(2) > ul > li > a.survey-button").click()
except:
    print("[Auto-HCS Error Handler] An Error Occurred! : 내부 프로그램 오류! 다시 시도하여주세요")

try:
    result = driver.switch_to.alert
    print("[Auto-HCS Error Handler] An Error Occurred! : "+result.text)
except:
    driver.find_element("css selector", "#survey_q1a1").click()
    driver.find_element("css selector", "#survey_q2a3").click()
    driver.find_element("css selector", "#survey_q3a1").click()
    driver.find_element("css selector", "#btnConfirm").click()

    if driver.find_element("css selector", "#container > div > div.contents > div.guide_center > p:nth-child(3) > span").text == "Check is completed.":
        print("[Auto-HCS info]" + driver.find_element("css selector", "#container > div > div.contents > div.guide_center > p:nth-child(1) > span").text + ' : ' + driver.find_element("css selector", "#container > div > div.contents > div.guide_center > p:nth-child(2)").text)

driver.quit()
system('pause')