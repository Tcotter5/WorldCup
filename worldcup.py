# pip install requests
# pip install beautifulsoup4
# pip install pretty printer (get a better idea of where to call on html file upon first scrape)
import pprint

from bs4 import BeautifulSoup
import requests

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
print(links)





