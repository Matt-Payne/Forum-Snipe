# Forum-Snipe
This is a series of scripts to scrape information from varying formus containing sports memorabilia 

## Table of Contents
* [General info](#general-information)
* [Technologies](#technologies)
* [Setup](#setup)
* [Documenation](#documentation)

## General Information
The aim of this script is to be able to quickly parse new card posts and send them out to people who want quick updates 
without having to constantly check on their own. Waiting for the sites automated system which can take an incredibly long
time.

## Technologies
Project is created with:
- Python 3.8
- BeautifulSoup
- Selenium

## Setup
To use these scripts properly follow the documentation below outlining how each part of the code works

## Documentation 

### `URLScraper.py`
This script can be used to create new scripts to scrape with on new forums using a very generalized system that can be 
reworked for most selling formus
```python
    def __init__(self, link):
        # Takes provided link and uses it as the base to scrape from

    def login(self,login_url,login_payload):
        # If the site requires a login this can be called to activate it

    def soup_finder(self):
        # Grabs the html converted to beautifulsoup format for future use

    def scrape_title_message(self, soup):
        # Grabs the title and the message using a provided soup

    def scrape_images(self, soup, website):
        # Grabs any images provided in the selling post and returns them as a list of their source links
        
    def scrape_username(self, soup):
        # Grabs the username of the poster

    def scrape_message_link(self, soup, website):
        # Grabs a link to private message the poster
```

### `Net54.py`
This script is used to scrape https://www.net54baseball.com/ specifically

```python
    def scrape_message_link(self, soup):
        # Grabs a link to message the user provided an html formatted soup of the post

    def scrape_time_date(self, soup):
        # Grabs the time and the date of the post provided an html formatted soup of the post

    def scrape_username(self, soup):
        # Grabs the username of the poster provided an html formatted soup of the post

    def scrape_images(self, soup):
        # Grabs all the links to the images in the post and returns them as a list provided an html formatted soup of 
        # the post

    def scrape_title_message(self, soup):
        # Grabs and returns the title and message of the post provided an html formatted soup of the post

    def login(self,login_url,login_payload):
        # Posts the login material to a provided login url

    def soup_finder(self):
        # Grabs the soup from a provided link in the initializer
```

### `Blowout.py`
This script scrapes https://www.blowoutforums.com/ for information on card sales
. This script requires the use of the custom `chromedriver.exe` which bypasses the bot detection system

```python
    def __int__(self, driver):
        # Initalizes the driver for the selenium instance

    def change_post(self, link):
        # Grabs a new post with the provided link using a set delay to prevent detection

    def scrape_title_message(self, soup):
        # Grabs the title and message using a soup instance parsed from the page

    def scrape_message_link(self, soup, website="www.blowoutforums.com/"):
        return URLScraper.URLScraper.scrape_message_link(self, soup, website)

    def scrape_time_date(self, soup):
        # Grabs the date and time using a soup instance parsed from the page

    def scrape_images(self, soup, website='www.blowoutforums.com/'):
        # Grabs the image links from the soup parsed webpage 
```
