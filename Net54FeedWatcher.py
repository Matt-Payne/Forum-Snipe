import URLScraper
import requests
from bs4 import BeautifulSoup as bs
s = requests.session()

login_payload = {
    'vb_login_username': 'Goudey',
    'vb_login_password': 'mattpayne123',
    'cookieuser': 1,
    'securitytoken': 'guest',
    'do': 'login',
    'vb_login_md5password': '0c3306cb8cb120406580ec159e1af70f',
    'vb_login_md5password_utf': '0c3306cb8cb120406580ec159e1af70f'
}
class Net54FeedWatcher:

    def __init__(self, link):
        self.link = link
        self.forum_links = []
        try:
            file = open('Net54_links', 'r')
            self.forum_links = file.readlines()
        except:
            pass

    def login(self, login_link, login_payload):
        login_req = s.post('https://www.net54baseball.com/login.php?do=login', data=login_payload)

    def scrape_posts(self, forum_link):
        soup = bs(s.get(forum_link).text, 'html.parser')

        posts = soup.find_all(
            lambda tag: tag.name == 'a' and tag.has_attr('id') and tag.has_attr('href') and 'thread_title_' in tag[
                'id'])
        file = open('Net54_links', 'a')
        for post in posts:
            if self.forum_links.__contains__('https://www.net54baseball.com/' + post.get('href')):
                break
            else:
                file.write('https://www.net54baseball.com/' + post.get('href') + '\n')
        file.close()



# 'https://www.net54baseball.com/login.php?do=login'