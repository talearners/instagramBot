# Channel : Ta Learners

from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from json import dump , load
from os.path import exists


class InstagramBot:
    driverpath = None

    def __init__(self) -> None:
        self.driver = Firefox(executable_path=self.driverpath)
        self.driver.find_element
    

    def login(self):
        self.driver.get("https://instagram.com")
        if not exists('./Cookies/ig.json'):
            navbar = '/html/body/div[1]/div/div/section/nav/div[2]/div/div'
            try:
                check_login = WebDriverWait(self.driver,60).until(
                    exp.presence_of_element_located((By.XPATH,navbar))
                )
                cookie = self.driver.get_cookies()
                with open("Cookies/ig.json",'w') as file:
                    dump(cookie,file)
                print("[+] Done To Get Cookies ... ")
            except:
                print('Error')
        else:
            with open('./Cookies/ig.json','r') as _file:
                for i in load(_file):
                    self.driver.add_cookie(i)
                
                self.driver.refresh()
                print("[+] login Successfully.....")