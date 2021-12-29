from selenium import webdriver


if __name__ == '__main__':
    with open('config.txt') as f:
        USERNAME, PASSWORD = f.readlines()
        USERNAME = USERNAME.rstrip()

    browser = webdriver.Chrome('chromedriver.exe')

    # Login to linkedin
    browser.get('https://www.linkedin.com/login')
    elem = browser.find_element_by_name("session_key")
    elem.send_keys(USERNAME)
    elem = browser.find_element_by_name("session_password")
    elem.send_keys(PASSWORD)
    elem.submit()

    # Direct to the Create a Post View
    browser.find_element_by_id('ember44').click()
