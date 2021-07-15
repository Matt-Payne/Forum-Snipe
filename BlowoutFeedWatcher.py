from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome('C:/Users/pamjw/Desktop/chromedriver.exe')
f = open("blowout_links.txt", "a")
links = []
links_written = []

while True:
    f = open("blowout_links.txt", "a")
    driver.get('https://www.blowoutforums.com/forumdisplay.php?f=29')
    feed = driver.page_source
    soup = bs(feed, 'html.parser')
    first_title = soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('id') and 'thread_title_' in tag['id'])
    first_name = first_title[7].get_text()
    print(first_name)
    if links.__contains__('www.blowoutforums.com/'+first_title[7].get('href')):
        pass
    else:
        links.append('www.blowoutforums.com/'+first_title[7].get('href'))
        for link in links:
            if links_written.__contains__(link):
                pass
            else:
                f.write(link + '\n')
                links_written.append(link)
        f.close()
    sleep(60)
    f = open("blowout_links.txt", "a")
    driver.get('https://www.blowoutforums.com/forumdisplay.php?f=29')
    rss = driver.page_source
    soup = bs(feed, 'html.parser')
    first_title = soup.find_all(
        lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('id') and 'thread_title_' in tag['id'])
    first_name_check = first_title[7].get_text()
    print(first_name_check)
    if first_name == first_name_check:
        print('No Update')
        pass
    else:
        i = 0
        for title in first_title:
            i+=1
            if first_name.title != first_name and i>7:
                if links.__contains__('www.blowoutforums.com/'+title.get('href')):
                    pass
                else:
                    links.append('www.blowoutforums.com/'+title.get('href'))
        print('Update Detected')
        for link in links:
            if links_written.__contains__(link):
                pass
            else:
                f.write(link + '\n')
                links_written.append(link)
        f.close()
