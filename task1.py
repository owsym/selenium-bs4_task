from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@zusmani78/videos")

last_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_scroll_height == last_scroll_height:
        break
    last_scroll_height = new_scroll_height

driver.quit()
