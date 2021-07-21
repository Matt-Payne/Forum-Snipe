from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs



class FeedWatcher:

    # Parameters
    # url: link to the forum page to be watched
    # time: time in seconds the program will wait when refreshing to check if a change has occurred
    # driver: selenium driver location use the provided github driver to bypass anti bot feature
    # filename: name of file that will be written to with the links
    # position_of_non_sticky: how many down counting from 0 that the first non sticky thread is located on the page

    def __init__(self, url, time, driver, filename, position_of_non_sticky):
        self.url = url
        self.time = time
        self.driver = driver
        self.links = []
        self.links_written = []
        self.filename = filename
        self.file = open(filename, "a")
        self.position_of_non_sticky = position_of_non_sticky

    # Opens file
    def file_open(self):
        self.file = open(self.filename, "a")

    # Sleeps for a set amount of seconds
    def sleep_time(self):
        sleep(self.time)

    # Checks if a link has already been written
    def link_check(self, url_link, first_thread_title):
        if self.links.__contains__('www.blowoutforums.com/' + first_thread_title[self.position_of_non_sticky].get('href')):
            pass
        else:
            self.links.append('www.blowoutforums.com/' + first_thread_title[self.position_of_non_sticky].get('href'))
            for url in self.links:
                if self.links_written.__contains__(url):
                    pass
                else:
                    self.file.write(url + '\n')
                    self.links_written.append(url)
            self.file.close()
            self.file_open()

    # Checks if there has been an update
    def titles_check(self, first_thread_title, second_thread_title, thread_titles_second_scan):
        if first_thread_title == second_thread_title:
            pass
        else:
            i = 0
            for thread_title in thread_titles_second_scan:
                i += 1
                if thread_title.get_text() != first_thread_title and i > self.position_of_non_sticky:
                    if self.links.__contains__('www.blowoutforums.com/' + thread_title.get('href')):
                        pass
                    else:
                        self.links.append('www.blowoutforums.com/' + thread_title.get('href'))
            for url in self.links:
                if self.links_written.__contains__(url):
                    pass
                else:
                    self.file.write(url + '\n')
                    self.links_written.append(url)
            self.file.close()
            self.file_open()

    # Scrapes actual info and provides to supplement classes
    def main_scrape(self):
        self.driver.get(self.url)
        current_feed = self.driver.page_source
        soup = bs(current_feed, 'html.parser')
        thread_titles_first_scan = soup.find_all(
            lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('id') and 'thread_title_' in tag[
                'id'])
        first_thread_title = thread_titles_first_scan[self.position_of_non_sticky].get_text()
        self.sleep_time()
        # Next Check
        self.driver.get(self.url)
        second_feed = self.driver.page_source
        soup = bs(second_feed, 'html.parser')
        thread_titles_second_scan = soup.find_all(
            lambda tag: tag.name == 'a' and tag.has_attr('href') and tag.has_attr('id') and 'thread_title_' in tag[
                'id'])
        second_thread_title = thread_titles_second_scan[self.position_of_non_sticky].get_text()
        self.titles_check(first_thread_title, second_thread_title, thread_titles_second_scan)


