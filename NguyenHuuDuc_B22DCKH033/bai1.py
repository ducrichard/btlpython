import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



url = "https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats"


response = requests.get(url)
soup = bs(response.text, "html.parser")


table = soup.find_all("table")
for item in table:
    headers = item.find_all("tr")[1]
    columns = [th.title for th in headers.find_all("th")]

players_data = []

for item in table:
    for row in item.find_all("tr"):
        player = {}
        cells = row.find_all("td")
    

    minutes_played = player.get("Min")
    if minutes_played and int(minutes_played) > 90:
        players_data.append(player)


df = pd.DataFrame(players_data, columns=['Player', 'Nation', 'Squad', 'Pos', 'Age', 'MP', 'Starts', 'Min', 'Gls', 'Ast', 'CrdY', 'CrdR', 
         'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR', 'Gls_90', 'Ast_90', 'G+A_90', 'G-PK', 'G+A-PK', 'xG_90', 'xAG_90', 'xG+xAG', 'npxG_90', 'npxG+xAG'])



df.fillna("N/a", inplace=True)

df = df.sort_values(by=['Player', 'Age'], ascending=[True, False])
print(df)
df.to_csv("results.csv", index=False)
