import time

def scroll_all_pages(driver):

    last_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(7)
        new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_scroll_height == last_scroll_height:
            break
        last_scroll_height = new_scroll_height

def extract_YT_video_data(soup):
    all_video_data = soup.find_all('ytd-rich-item-renderer')
    extracting_data = []
    for video in all_video_data:
        title = video.find('yt-formatted-string', {"id": "video-title"}).text
        views = video.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
        upload_time = video.find(
            'span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}
        ).get('before')
        video_duration = video.find(
            'span', {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}
        ).text.strip()
        video_thumbnails = video.find('img', {"style": "background-color: transparent;"}).get('src')

        extracted_video_data = {
            "Title": title,
            "Views": views,
            "Video Duration": video_duration,
            "Upload Time": upload_time,
            "Thumbnails": video_thumbnails
        }
        extracting_data.append(extracted_video_data)
    return extracting_data
