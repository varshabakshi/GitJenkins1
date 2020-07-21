from selenium import webdriver

import time
from selenium.webdriver.common.keys import Keys
def test_verify():
    print("sample test case started")
    driver = webdriver.Chrome(r'C:/Users/varsha_bakshi/Downloads/chromedriver_win32/83_0_4103/chromedriver.exe')
    #driver=webdriver.firefox()
    #driver=webdriver.ie()
    time.sleep(3)
    #maximize the window size
    driver.maximize_window()
    #navigate to the url
    driver.get("https://www.google.com/")
    #identify the Google search text box and enter the value
    driver.find_element_by_name("q").send_keys("javatpoint")
    time.sleep(3)
    #click on the Google search button
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    time.sleep(3)
    #close the browser
    driver.close()
    print("sample test case successfully completed")

    def test_verify2():
        print("sample test case started")
        driver = webdriver.Chrome(r'C:/Users/varsha_bakshi/Downloads/chromedriver_win32/83_0_4103/chromedriver.exe')
        # driver=webdriver.firefox()
        # driver=webdriver.ie()
        time.sleep(3)
        # maximize the window size
        driver.maximize_window()
        # navigate to the url
        driver.get("https://www.google.com/")
        # identify the Google search text box and enter the value
        driver.find_element_by_name("q").send_keys("javatpoint")
        time.sleep(3)
        # click on the Google search button
        driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
        time.sleep(3)
        # close the browser
        driver.close()
        print("sample test case successfully completed")