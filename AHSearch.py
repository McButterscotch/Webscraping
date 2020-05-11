from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.ah.nl/'

def Search(url, key_word):
    """This function searches for keywords on the site of Albert Heijn. Its output is a new url"""
    return url + 'zoeken?query='+ key_word

def Pagefinder(url):
    """This function opens and stores and html page. Its output is already parsed"""
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, 'html.parser')

def Productfinder(page_soup):
    """This function finds all the products on the search page"""
    return page_soup.findAll('a', {'class':'link_root__1r7dk'})

# Unfortunately, this function cant tell the difference between new and old prices
def Pricefinder(page_soup):
    """This function finds all the prices on the search page"""
    price_int_ls, price_ft_ls = page_soup.findAll('span', {'class':'price-amount_integer__y84AA'}), page_soup.findAll('span', {'class':'price-amount_fractional__OONsC'})

    price_ls = []
    # My beautiful loop to get the prices
    for i in range(len(price_int_ls)):
        price_int = str(price_int_ls[i].text)
        price_ft = str(price_ft_ls[i].text)
        price_ls.append( price_int + '.' + price_ft)
    return price_ls

search = str(input('What are you looking for?'))

# Search URL
my_new_url = Search(my_url, search)
page_soup = Pagefinder(my_new_url)
prodContainer = Productfinder(page_soup)

# Prints all the products
for i in prodContainer:
    title_container  = str(i.get('title'))
    print(title_container)

