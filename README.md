## Web Scrapping Box Office Mojo data with Python - Beautiful Soup

### Overview
This is a script for scrapping box office data from the Box office Mojo website and creating a csv file for the data.
The script scraps data from the Box office Mojo website [link provided below]. The data is scrapped into a list of 
dictionaries that contain the `movie title`, `box office earnings`, `moving ranking`, and `release year`.

link: https://www.boxofficemojo.com/title/tt0499549/?ref_=bo_cso_table_1
Data: `movie data/Top Lifetime Grosses.csv`

### Project Steps:
The project took numerous steps, including the following
+ Importing modules - bs4, requests, pandas, etc
+ Obtaining html data from the Box office Mojo website,
+ Creating a Beautiful Soup Object,
+ Parsing html text data into the bs4 object,
+ Accessing specific tags, especially the ones containing the needed data - a function created for that purpose,
+ Assigning data to variables for each record using a loop
+ Turning the dictionary created into a pandas dataframe

### Primary Tools Used:
+ Beautiful Soup 4,
+ lxml parser,
+ Requests objects,
+ Python Pandas.

### Author:
= Julius Charles