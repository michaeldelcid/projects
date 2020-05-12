#Website contains all Team Data for 2018 - 2019 Season 
#https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2018-19&SeasonType=Regular%20Season

from selenium import webdriver
from pandas import *
import pandas 
import numpy as np 
import matplotlib.pyplot as plt
from sqlalchemy import *

path_to_chromedriver = 'C:\Eclipse\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_to_chromedriver)

year = '2018-19'

# Navigate to NBA Team Stats, default season is 2019 - 2020 season
url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1'

driver.get(url)
       
table = driver.find_element_by_class_name('nba-stat-table__overflow')

team_ids = []
team_name = []
team_stats = []

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id == 0:
        column_names = lines.split(' ')[1:]
    else:
        if line_id % 3 == 1:
            team_ids.append(lines)
        if line_id % 3 == 2:
            team_name.append(lines)
        if line_id % 3 == 0:
            team_stats.append( [float(i) for i in lines.split(' ')] )
            
team_db = pandas.DataFrame({'Team': team_name,
                       'GP': [i[0] for i in team_stats],
                       'W': [i[1] for i in team_stats],
                       'L': [i[2] for i in team_stats],
                       'WIN%': [i[3] for i in team_stats], 
                       'MIN': [i[4] for i in team_stats],
                       'PTS': [i[5] for i in team_stats],
                       'FGM': [i[6] for i in team_stats],
                       'FGA': [i[7] for i in team_stats],
                       'FG%': [i[8] for i in team_stats],
                       '3PM': [i[9] for i in team_stats],
                       '3PA': [i[10] for i in team_stats],
                       '3P%': [i[11] for i in team_stats],
                       'FTM': [i[12] for i in team_stats],
                       'FTA': [i[13] for i in team_stats],
                       'FT%': [i[14] for i in team_stats],
                       'OREB': [i[15] for i in team_stats],
                       'DREB': [i[16] for i in team_stats],
                       'REB': [i[17] for i in team_stats],
                       'AST': [i[18] for i in team_stats],
                       'TOV': [i[19] for i in team_stats],
                       'STL': [i[20] for i in team_stats],
                       'BLK': [i[21] for i in team_stats],
                       'BLKA': [i[22] for i in team_stats],
                       'PF': [i[23] for i in team_stats],
                       'PFD': [i[24] for i in team_stats],
                       '+/-': [i[25] for i in team_stats]
                       }
                     ) 
#Prints All 30 Team Stats for a given season
print(team_db)

#Plot Team FGA vs. FG%

plt.scatter(team_db['FGA'],team_db['FG%'])
plt.xlabel('Field Goals Attempted (per game)', fontsize=16, fontweight= 'bold')
plt.ylabel('Field Goal % (per game)', fontsize=16, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
plt.xlim([80,95])
plt.ylim([42, 50])
plt.show()

#Plot Team FG% vs. Win or NBA standing

plt.scatter(team_db['FG%'],team_db['W'])
plt.xlabel('Field Goals % (per game)', fontsize=16, fontweight= 'bold')
plt.ylabel('Number of wins (per season)', fontsize=16, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
plt.xlim([42,50])
plt.ylim([10, 82])
plt.show()


# Port NBA player DATA



