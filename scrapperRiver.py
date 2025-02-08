import requests
from bs4 import BeautifulSoup
import pandas as pd
import LanusStats as ls  

# URL del sitio web
url = "https://www.promiedos.com.ar/team/river-plate/igi"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, "html.parser")

    fechas = soup.find_all("td", class_="td_table_td_col__UdgoO td_bold__rJ5vf td_startTeam__eCpwP")
    loc_o_vic=soup.find_all("td", class_="td_table_td_col__UdgoO td_bold__rJ5vf td_border__bFkDF td_content__yqb6C")
    rival=soup.find_all("div", class_="table_team_block__y6rYP team-block")
    hora=soup.find_all("td", class_="td_table_td_col__UdgoO td_bold__rJ5vf td_content__yqb6C")



transfermarkt = ls.Transfermarkt()

santi= transfermarkt.get_player_played_data("Santiago Simón","661131")

# Convert the data to a DataFrame
df = pd.DataFrame(santi)

# Print the last row and the fifth column
partidos_jugados=df.iloc[-1, 5]

print(partidos_jugados)