import requests
from bs4 import BeautifulSoup as bs

s = requests.session()

#  Parameters:
#  link = url destination to forum page that is being scraped for information
#  Class takes link and outputs data into database
#  Example: temp = ScrappingModule('https://www.net54baseball.com/showthread.php?t=304362')


class URLScraper:

    def __init__(self, link):
        self.link = link

    def login(self,login_url,login_payload):
        # Login Credentials
        login_req = s.post(login_url, data=login_payload)

    def soup_finder(self):
        # Grabbing Title and Message
        soup = bs(s.get(self.link).text, 'html.parser')
        return soup

    def scrape_title_message(self, soup):
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id'))
        id = table.get('id')
        id = id[4::]

        # Grabbing title
        title = soup.find_all('strong')[0].get_text()
        title = title.strip()

        # Grabbing Message
        message = soup.find(lambda tag: tag.has_attr('id') and tag['id'] == 'post_message_' + id).get_text()
        message = message.strip()
        return title, message

    def scrape_images(self, soup, website):
        # Grabbing Links to Images
        image_links = soup.find_all(lambda tag: tag.name == 'img' and tag.has_attr('class'))
        links_list = []
        for tags in image_links:
            if tags.get('class')[0] == "attach":
                if 'www.' in tags.get('src'):
                    links_list.append(tags.get('src').__str__())
                else:
                    links_list.append(website+tags.get('src'))
        return links_list

    def scrape_username(self, soup):
        # Grabbing Username
        username = soup.find(lambda tag: tag.name == 'a' and tag.has_attr('class') and tag['class'][0] == "bigusername")
        username = username.get_text()
        return username

    def scrape_message_link(self, soup, website):
        # Grabbing link to message user
        username_message_link = soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('rel') and tag['rel'][0] == "nofollow")
        for check in username_message_link:
            if "Send a private message to" in check.get_text():
                username_message_link = website+check.get('href')
        return username_message_link

    def scrape_time_date(self, soup):
        # Grabbing data and time of post
        date_time = soup.find_all(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'][0] == "normal")
        for temp in date_time:
            if "AM" in temp.get_text() or "PM" in temp.get_text():
                date_time = temp.get_text().strip()
        return date_time


