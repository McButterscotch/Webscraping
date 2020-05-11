from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.ah.nl/producten'

# Open de page
uClient = uReq(my_url)

# Store page
page_html = uClient.read()

# Close the page
uClient.close()

# Parse
page_soup = soup(page_html, 'html.parser')

# Load all the categories from the site.
catContainers = page_soup.findAll('div', {'class' : 'product-category-overview_category__E6EMG'})

# Select the first category (Aardappels, Groente en Fruit), and print a few products
# This contains the first catagory of the list
cat_1 = catContainers[0]

# Tries to find the href, link to the next page
for link in cat_1.findAll('a'):
    href = link.get('href')

# urls is updated, we can navigate to a new page
my_new_url = 'http://www.ah.nl' + href

# Same routine as before
uClient = uReq(my_new_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

# This finds all products
# All products are listed twice for some reason
prodContainers = page_soup.findAll('a', {'class': 'link_root__1r7dk'})

# Prints all the products in the catagory
for i in prodContainers:
    title_container = i.get('title')
    print(title_container)

