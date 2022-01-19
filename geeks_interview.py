
from selenium import webdriver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def open_geeks(path, leet_user, leet_pass):
    
    try:
        # browser = webdriver.Firefox()
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(path)


        # open a new tab
        # then switch to new tab
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])

        #open the login page of leetcode in browser
        browser.get("https://leetcode.com/accounts/login/")

        time.sleep(10)

        #select the username field and enter the user name
        elem = browser.find_element_by_css_selector("#id_login")
        elem.send_keys(leet_user)

        # select the password field and enter the password
        elem = browser.find_element_by_css_selector("#id_password")
        elem.send_keys(leet_pass)

        # time.sleep(10)

        #press the sign in button
        elem = browser.find_element_by_css_selector(".btn-content-container__2HVS")
        elem.click()

        time.sleep(10)

        #after sign in go to problems page, now you are ready to practice
        elem = browser.find_element_by_css_selector(".navbar-left-container__3-qz > div:nth-child(3)")
        elem.click()


        # to prevent from closing the python script
        input("press anything to exit ")

        # close the browser
        browser.close()
        browser.quit()
    except:
        print("Please check your internet connection")


