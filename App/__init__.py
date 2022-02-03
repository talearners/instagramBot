'''
Author : TA Learners 

'''

from cProfile import label
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import TimeoutException
from json import dump , load
from os.path import exists
from time import sleep


class InstagramBot:
    driverpath = None

    def __init__(self) -> None:
        self.driver = Firefox(executable_path=self.driverpath)
    

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

        sleep(5)

        try:
            popup = WebDriverWait(driver=self.driver,timeout=60).until(
                exp.presence_of_element_located((By.XPATH,"/html/body/div[6]/div/div/div/div[3]/button[2]"))
            )
            if popup.text == "Not Now":
                popup.click()
                print("[+] Clicked Not Now in Notification Popup")
        
        except Exception as e:
            pass
        
        sleep(5)


    def Do_like(self):
        try:
            article = WebDriverWait(self.driver,60).until(
                exp.presence_of_all_elements_located((By.TAG_NAME,"article")),
                str("[!] article Elements Not Found !\n Run Again !")
            )
            section = [sec.find_element_by_tag_name('section') for sec in article]
            button  = [btn.find_elements_by_tag_name('button') for btn in section]
            self.driver.execute_script("""
            scrollBy({top:Math.floor(Math.random() * 100)+200,behavior:'smooth'})""")
            
            for btn in button:
                label = btn[0].find_element_by_tag_name('svg').get_attribute('aria-label')
                if label != 'Like':
                    print("[+]Already Liked...")
                    continue
                self.driver.execute_script("""scrollBy({top:Math.floor(Math.random() * 100)+900,behavior:'smooth'})""")
                sleep(3)
                btn[0].click()
                print("[+] Like On Post ..")
                sleep(2)

            self.driver.refresh()
        except TimeoutException as timeout:
            print(timeout.msg)