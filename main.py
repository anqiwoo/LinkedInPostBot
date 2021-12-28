from selenium import webdriver
import time


if __name__ == '__main__':
    with open('config.txt') as f:
        USERNAME, PASSWORD = f.readlines()
        USERNAME = USERNAME.rstrip()

    browser = webdriver.Chrome('chromedriver.exe')

    # elementID = browser.find_element_by_id('username')
    # elementID.send_keys(USERNAME)
    # elementID = browser.find_element_by_id('password')
    # elementID.send_keys(PASSWORD)
    # elementID.submit()

    # Login to linkedin
    browser.get('https://www.linkedin.com/login')
    elem = browser.find_element_by_name("session_key")
    elem.send_keys(USERNAME)
    elem = browser.find_element_by_name("session_password")
    elem.send_keys(PASSWORD)
    elem.submit()
    # c = browser.find_element_by_id("login-submit")
    # c.click()

    # Learn how to add arguments to start this script in command line
    # text = 'For LinkinedIn Bot Test.'

    # browser.find_element_by_class_name("ql-editor.ql-blank").send_keys(text)
    # time.sleep(1)
    # browser.find_element_by_id('ember500').click()
    browser.find_element_by_id('ember44').click()
    # browser.find_element_by_class_name(
    #     'share-creation-state__text-editor').send_keys(text)
    # browser.find_element_by_id("ember500")

    # post_box = browser.find_element_by_class_name(
    #     "sharing-create-share-view__create-content")
    # post_box.click()
    # sleep(2)
    # mes = browser.find_element_by_class_name(
    #     "mentions-texteditor__contenteditable")
    # mes.send_keys(message)
    # sleep(2)
    # post_box = browser.find_element_by_xpath(
    #     "//*[@data-control-name='share.post']")
    # post_box.click()
    # sleep(2)
    # print('Posted!')
    # browser.quit()
    # print('End!')
