# pip install requests
# pip install beautifulsoup4
# pip install pretty printer (get a better idea of where to call on html file upon first scrape)
import pprint
# pip install panadas
# pip install lxml
# pip install html5lib

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://fbref.com/en/comps/1/schedule/World-Cup-Scores-and-Fixtures"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# find table via inspect tool / search on first instance of class name stats_table using 0
table = doc.select('table.stats_table')[0]

# find all instances of a within html file
links = table.find_all('a')

# grab hrefs
links = [l.get("href") for l in links]

# filter links to only get squad links via list comprehension, "is squad in link/ if not do not retrieve"
links = [l for l in links if '/squads/' in l]

# add additional https: to partial urls from before
squad_urls = [f"https://fbref.com{l}" for l in links]

# get first link
squad_urls = squad_urls[0]

result = requests.get(squad_urls)

matches = pd.read_html(result.text, match="Home & Away")

print(matches)









