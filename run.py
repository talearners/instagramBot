'''
Author  : TA Learners
'''

from App import InstagramBot


if __name__ == "__main__":
    InstagramBot.driverpath = "./Driver/geckodriver.exe"
    instagram = InstagramBot()
    instagram.login()
    while True:
        instagram.Do_like()