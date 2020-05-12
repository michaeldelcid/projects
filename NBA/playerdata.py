#Website contains all Team Data for 2019 - 2020 Season 
#https://stats.nba.com/leaders/https://stats.nba.com/leaders/

from selenium import webdriver
from pandas import *
import pandas 
import numpy as np 
import matplotlib.pyplot as plt
from sqlalchemy import *


path_to_chromedriver = 'C:\Eclipse\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)

# Navigate to NBA Team Stats, default season is 2019 - 2020 season

player_url = 'https://stats.nba.com/leaders/https://stats.nba.com/leaders/'
driver.get(player_url)
 
#Team stats table
table = driver.find_element_by_class_name('nba-stat-table__overflow')

#Parsing thru team data
player_ids = []
player_name = []
player_stats = []

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    else:
        if line_id % 3 == 1:
            player_ids.append(lines)
        if line_id % 3 == 2:
            player_name.append(lines)
        if line_id % 3 == 0:
            player_stats.append( [float(i) for i in lines.split(' ')] )
            
player_db = pandas.DataFrame({'player': player_names,
                       'gp': [i[0] for i in player_stats],
                       'min': [i[1] for i in player_stats],
                       'pts': [i[2] for i in player_stats],
                       'fgm': [i[3] for i in player_stats], 
                       'fga': [i[4] for i in player_stats],
                       'fg%': [i[5] for i in player_stats],
                       '3pm': [i[6] for i in player_stats],
                       '3pa': [i[7] for i in player_stats],
                       '3p%': [i[8] for i in player_stats],
                       'ftm': [i[9] for i in player_stats],
                       'fta': [i[10] for i in player_stats],
                       'ft%': [i[11] for i in player_stats],
                       'oreb': [i[12] for i in player_stats],
                       'dreb': [i[13] for i in player_stats],
                       'reb': [i[14] for i in player_stats],
                       'ast': [i[15] for i in player_stats],
                       'stl': [i[16] for i in player_stats],
                       'blk': [i[17] for i in player_stats],
                       'tov': [i[18] for i in player_stats],
                       'eff': [i[19] for i in player_stats]
                       }
                     )

#Remove comment  if you want to save team_db to a csv file
player_db.to_csv(r'C:\projects\NBA\teamdata.csv', index = False, header=True)

print(player_db)
