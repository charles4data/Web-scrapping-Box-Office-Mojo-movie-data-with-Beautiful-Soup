# import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


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


# Selecting specific tr class
def has_target_class(tr):
    return tr.name == 'tr' and tr.find('td', class_='a-text-right mojo-header-column mojo-truncate '
                                                    'mojo-field-type-rank')


# Accessing the data and assigning to a pandas dataframe
gross_data = pd.DataFrame()
index = 0
target_tags = soup.find_all(has_target_class)
for target_tag in target_tags:
    movie_rank = target_tag.find('td', class_='a-text-right mojo-header-column mojo-truncate mojo-field-type-rank')
    movie_name = target_tag.find('td', class_='a-text-left mojo-field-type-title')
    movie_link = target_tag.find('td', class_='a-link-normal')
    lifetime_gross = target_tag.find('td', class_='a-text-right mojo-field-type-money')
    release_year = target_tag.find('td', class_='a-text-left mojo-field-type-year')

    # Creating and assigning variables for
    if target_tag:
        rank = movie_rank.text
        title = movie_name.text
        box_office = lifetime_gross.text
        year = release_year.text

        #assigning to a pandas dataframe
        for index in range(len(target_tags)):
            gross_data['Movie Rankings'] = rank
            gross_data['Title'] = title
            gross_data['Total Earnings'] = box_office
            gross_data['Release Year'] = year

print(gross_data)





