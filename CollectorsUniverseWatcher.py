import requests
from bs4 import BeautifulSoup as bs
s = requests.session()


class CollectorsUniverseWatcher:

    def __init__(self, link):
        self.link = link
        self.links_list = []

    def initialize(self):
        try:
            file = open('CollectorsUniverseLinks','r')
            self.links_list = file.readlines()
        except:
            pass

    def update_cache(self):
        file = open('CollectorsUniverseLinks','a')
        soup = bs(s.get(self.link).text, 'html.parser')
        posts = soup.find_all(lambda tag: tag.name == 'li' and tag.has_attr('id') and 'Discussion_' in tag['id'])
        for post in posts:
            post_link = post.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href'))
            if 'Forum Rules' not in post_link[1].get_text():
                if self.links_list.__contains__(post_link[1].get('href')):
                    print()
                else:
                    file.write(post_link[1].get('href')+'\n')
        file.close()


temp = CollectorsUniverseWatcher('https://forums.collectors.com/categories/buy-sell-trade-sports')
temp.update_cache()
