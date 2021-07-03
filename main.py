import requests
from bs4 import BeautifulSoup as bs

s = requests.session()


# Checks to see if its a post inside the selling area
def selling_check(soup):
    try:
        selling_forum = soup.find(lambda tag: tag.name == 'a' and tag.has_attr('href') and tag['href'] == "forumdisplay.php?f=3")
        if selling_forum.get_text() == 'Net54baseball Buy/Sell/Trade Section  (must login, caveat emptor)':
            return True
        else:
            return False
    except:
        pass
        return False


class ScrappingModule:

    def __init__(self, link):
        self.link = link

    def scrape(self):

        # Login Credentials
        login_payload = {
            'vb_login_username': 'Goudey',
            'vb_login_password': 'mattpayne123',
            'cookieuser': 1,
            'securitytoken': 'guest',
            'do': 'login',
            'vb_login_md5password': '0c3306cb8cb120406580ec159e1af70f',
            'vb_login_md5password_utf': '0c3306cb8cb120406580ec159e1af70f'
        }

        login_req = s.post('https://www.net54baseball.com/login.php?do=login', data=login_payload)

        #Grabbing Title and Message
        soup = bs(s.get(self.link).text, 'html.parser')

        if selling_check(soup):
            table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id'))
            id = table.get('id')
            id = id[4::]

            #Grabbing title
            title = soup.find_all('strong')[0].get_text()
            title = title.strip()

            #Grabbing Message
            message = soup.find(lambda tag: tag.has_attr('id') and tag['id'] == 'post_message_' + id).get_text()
            message = message.strip()

            #Grabbing Links to Images
            image_links = soup.find_all(lambda tag: tag.name == 'img' and tag.has_attr('class'))
            links_list = []
            for tags in image_links:
                if tags.get('class')[0] == "attach":
                    if  'www.' in tags.get('src'):
                        links_list.append(tags.get('src').__str__())
                    else:
                        links_list.append("www.net54baseball.com/"+tags.get('src'))

            #Grabbing Username
            username = soup.find(lambda tag: tag.name == 'a' and tag.has_attr('class') and tag['class'][0] == "bigusername")
            username = username.get_text()

            #Grabbing link to message user
            username_message_link = soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('rel') and tag['rel'][0] == "nofollow")
            for check in username_message_link:
                if "Send a private message to" in check.get_text():
                    username_message_link = "www.net54baseball.com/"+check.get('href')

            #Grabbing data and time of post
            date_time = soup.find_all(lambda tag: tag.name == 'div' and tag.has_attr('class') and tag['class'][0] == "normal")
            for temp in date_time:
                if "AM" in temp.get_text() or "PM" in temp.get_text():
                    date_time = temp.get_text().strip()


            file_write = {
                'Date & Time': date_time,
                'Title': title,
                'Message': message,
                'Image Links': links_list,
                'Username': username,
                'Private Message Link': username_message_link

            }

            # ,; = delimiter
            f = open("temp.txt", "w")
            f.write(file_write.get('Date & Time')+",;"+file_write.get('Title')+",;"+file_write.get('Message') + ",;" +
                    file_write.get('Image Links').__str__()+",;"+file_write.get('Username')+",;"+'www.net54baseball.com/' +
                    file_write.get('Private Message Link')+"\n")
            f.close()


temp = ScrappingModule('https://www.net54baseball.com/showthread.php?t=304362')
temp.scrape()
