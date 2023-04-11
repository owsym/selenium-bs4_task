from utils import scroll_all_pages,extract_YT_video_data
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

channel_link = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome()
driver.get(channel_link)

scroll_all_pages(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

extracted_video_data = extract_YT_video_data(soup)

data_frame = pd.DataFrame(extracted_video_data)
data_frame.to_csv('zusmani78.csv', index=False)

print('Extracted data successfully save to CSV file')
