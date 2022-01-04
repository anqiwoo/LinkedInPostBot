from selenium import webdriver
import time as t
import os
from PIL import Image
# Depending on your need, you can uncomment the last few lines of codes to save the screenshot of your today's post and open it for checking purpose.


if __name__ == '__main__':
    # Open the post.txt for you to edit the post content.
    os.startfile('post.txt')
    t.sleep(120)  # Leave 2 mins to check the post content.
    with open('config.txt') as f1, open('post.txt', encoding='utf-8') as f2:
        USERNAME, PASSWORD = f1.readlines()
        USERNAME = USERNAME.rstrip()
        POSTTEXT = f2.read()

    browser = webdriver.Chrome('chromedriver.exe')

    # Login to linkedin
    browser.get('https://www.linkedin.com/login')
    elem = browser.find_element_by_name("session_key")
    elem.send_keys(USERNAME)
    elem = browser.find_element_by_name("session_password")
    elem.send_keys(PASSWORD)
    elem.submit()

    # Direct to the Create a Post View
    browser.find_element_by_id('ember35').click()

    # Enter the Post Content
    t.sleep(2)
    postarea = browser.find_element_by_class_name("ql-editor.ql-blank")
    postarea.send_keys(POSTTEXT)

    # Press the Post Button
    t.sleep(2)
    browser.find_element_by_xpath(
        "//div[@class='share-box_actions']//span[@class='artdeco-button__text']").click()

    # # Save the Screenshot (Just for checking the post)
    t.sleep(2)
    # browser.save_screenshot("TodayPost.png")
    browser.quit()  # Close the browser
    print('\n\nEverything went well! Hooray!')

    # # Open up the png file for checking
    # img = Image.open('TodayPost.png')
    # img.show()
