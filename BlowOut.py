import URLScraper
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import random
import datetime

# To use selenium with this script please follow this link and execute the required steps
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver/41220267
# Driver also included in the git folder


class BlowOutScraper(URLScraper.URLScraper):

    def __int__(self, driver):
        self.driver = driver

    def change_post(self, link):
        time = random.randrange(1, 30, 1)
        sleep(time)
        self.driver.get(link)

    def scrape_title_message(self, soup):

        # Grabbing title
        title = soup.find_all('strong')[0].get_text()

        # Grabbing Message
        message = soup.find(lambda tag: tag.has_attr('id') and 'post_message_' in tag['id']).get_text()
        message = message.strip()
        return title, message

    def scrape_message_link(self, soup, website="www.blowoutforums.com/"):
        return URLScraper.URLScraper.scrape_message_link(self, soup, website)

    def scrape_time_date(self, soup):
        date_time = soup.find_all(lambda tag: tag.name == 'td' and tag.has_attr('class') and tag['class'][0] == 'thead')
        if'Yesterday' in date_time[4].get_text():
            date = datetime.date.today().day.real - 1
            time = date_time[4].get_text().strip()
            time = time.split(',')
            time = time[1]
            return datetime.date.today().month.__str__()+'/'+date.__str__()+'/'+datetime.date.today().year.__str__()+',' + time
        if 'Today' in date_time[4].get_text():
            time = date_time[4].get_text().strip()
            time = time.split(',')
            time = time[1]
            return datetime.date.__str__()+', '+time
        return date_time[4].get_text().strip()

    def scrape_images(self, soup, website='www.blowoutforums.com/'):
        links_list = []
        image_links = soup.find_all(lambda tag: tag.name == 'img' and tag.has_attr('src') and not tag.has_attr('class') and tag.has_attr('alt')
                                    and not tag.has_attr('title') and not tag.has_attr('id'))
        for links in image_links:
            if 'www.' in links.get('src'):
                links_list.append(links.get('src').__str__())
            else:
                links_list.append(website + links.get('src'))
            links_list.append(links.get('src'))
        return links_list



driver = webdriver.Chrome('C:/Users/pamjw/Desktop/chromedriver.exe')
driver.get('https://www.blowoutforums.com/showthread.php?t=1474975')
html = driver.page_source
soup = bs(html, 'html.parser')

temp = BlowOutScraper(driver)
print(temp.scrape_time_date(soup))

