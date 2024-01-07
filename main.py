# import necessary libraries
from bs4 import BeautifulSoup
import requests


# Getting text from url
url = "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"
response = requests.get(url)
if response.status_code == 200:
    html_text = response.text
else:
    print("Failed to fetch website content")
    exit()


# Parsing the html content to beautiful soup
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.find('table', class_='a-bordered a-horizontal-stripes a-size-base a-span12 mojo-body-table mojo-table-annotated scrolling-data-table')



print(movies)
