from utils import scroll_all_pages, extract_url_video_data
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

channel_url = input('Please enter your YouTube URL : ')

driver = webdriver.Chrome()
driver.get(channel_url)

scroll_all_pages(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

extracted_video_data = extract_url_video_data(soup)

data_frame = pd.DataFrame(extracted_video_data)
data_frame.to_csv(f"{channel_url.split('/')[-2]}.csv", index=False)

print('Extracted data successfully save to CSV file')
