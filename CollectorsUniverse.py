import URLScraper
import requests
from bs4 import BeautifulSoup as bs


# no login required
class CollectorsUniverse(URLScraper.URLScraper):
    def scrape_title_message(self, soup):
        message = soup.find_all(lambda tag: tag.name == 'p')
        message = message[0].get_text().strip()
        title = soup.find_all(lambda tag: tag.name == 'h1')
        title = title[0].get_text().strip()
        return title, message

    def scrape_images(self, soup):
        links_list = []
        images = soup.find_all(lambda tag: tag.name == 'img' and tag.has_attr('class') and tag['class'][0] == 'embedImage-img')
        for image in images:
            links_list.append(image.get('src'))
        return links_list

    def scrape_time_date(self, soup):
        time = soup.find_all(lambda tag: tag.name == 'time')
        time_date = time[0].get('title')
        return time_date

    def scrape_username(self, soup):
        username = soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('class') and len(tag['class']) >=1 and tag['class'][0] == 'Username')
        username = 'https://forums.collectors.com/'+username[0].get('href')
        return username


