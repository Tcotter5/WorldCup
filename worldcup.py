# pip install requests
# pip install beautifulsoup4
# pip install pretty printer (get a better idea of where to call on html file upon first scrape)
# pip install panadas
# pip install lxml
# pip install html5lib

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame


url = "https://fbref.com/en/comps/1/schedule/World-Cup-Scores-and-Fixtures"

# applying url to variable results via requests
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

# pass html (result.text) /  find specific string using match
match_table = pd.read_html(result.text, match="Scores & Fixtures")

# wanted to see all available columns, only showing 4 beforehand
# pd.options.display.max_columns = 14

print(match_table)
#print(match_table[0])



# ***** keeping old code commented out, not what I wanted to do but good to have for reference *******
# find table via inspect tool / search on first instance of class name stats_table using 0
# table = doc.select('table.stats_table')[0]

# find all instances of a within html file
# links = table.find_all('a')

# grab hrefs
# links = [l.get("href") for l in links]

# filter links to only get squad links via list comprehension, "is squad in link/ if not do not retrieve"
# links = [l for l in links if '/squads/' in l]

# add additional https: to partial urls from before
# squad_urls = [f"https://fbref.com{l}" for l in links]

# get first link
# squad_urls = squad_urls[0]

# matches = pd.read_html(result.text, match="Home & Away")










