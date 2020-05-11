from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup

# There is something weird with this site, it load more information form places I can't find


my_url = 'https://www.jumbo.com/'
hdr = {'User-Agent':'Mozilla/5.0'}

def Search(url, key_word):
    """This function searches for keywords on Jumbo's site. Its output is a new url"""
    return url + 'producten/?searchTerms='+ key_word + '&pageSize=25'

def Pagefinder(url, hdr):
    """This function opens and stores and html page. Its output is already parsed"""
    req = Request(url, headers=hdr)
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, 'html.parser')

def Productfinder(page_soup):
    """This function finds all the products on the search page"""
    return page_soup.findAll('a', {'class':'opposite'})

search = str(input('What are you looking for?'))

# Search URL
my_new_url = Search(my_url, search)
page_soup = Pagefinder(my_new_url, hdr)
prodContainer = Productfinder(page_soup)
print(prodContainer)