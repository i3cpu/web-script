from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import subprocess
import pyautogui 

driver = webdriver.Chrome('/path/to/chromedriver')

driver.get('https://www.youtube.com')


search_video = driver.find_element(By.NAME,'search_query') 

time.sleep(3)

search_video.send_keys('су')
search_video.send_keys(Keys.RETURN) 
time.sleep(4)

video = driver.find_element(By.XPATH, "//ytd-video-renderer[@class='style-scope ytd-item-section-renderer']//div[@id='dismissible']//ytd-thumbnail//a[@id='thumbnail']")
link = video.get_attribute('href')
print(link)
# driver.refresh()
driver.get(link)

 
search_video = driver.find_element(By.NAME,'search_query')
time.sleep(5)
search_video.send_keys('шпиливили крч')

share = driver.find_element(By.XPATH, "//ytd-button-renderer[@class='style-scope ytd-menu-renderer']//yt-button-shape//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading ']")
share.click()

time.sleep(5)
copy_link = driver.find_element(By.XPATH, "//yt-button-renderer[@id='copy-button']//yt-button-shape//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m ']")
copy_link.click()

subprocess.run('telegram-desktop')

time.sleep(7)
pyautogui.write('mirsadikovm', interval=0.0)
time.sleep(3)
pyautogui.keyDown('down')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
# pyautogui.typewrite('mirsadikovm', interval=0.0)
# time.sleep(3)
pyautogui.write(f'{link}', interval=0.0)
time.sleep(3)
pyautogui.press('enter')







time.sleep(50)


driver.quit()
