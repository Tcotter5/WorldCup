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
pd.options.display.max_columns = 14
#make a list in order out of match_table
table = match_table[1]
#extract contents wanted from table
table_two = table[['Date', 'Home', 'Score', 'Away', 'Attendance']]

print(table_two)












