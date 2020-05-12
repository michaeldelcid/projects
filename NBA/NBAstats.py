#Website contains all Team Data for 2019 - 2020 Season 
#https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1

from selenium import webdriver
from pandas import *
import pandas 
import numpy as np 
import matplotlib.pyplot as plt
import sys

#Enter chromedriver.exe installation path here
path_to_chromedriver = sys.argv[1] #Enter system argument as a string 
driver = webdriver.Chrome(executable_path=sys.argv[1])


# Navigate to NBA Team Stats, default season is 2019 - 2020 season
team_url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1'
driver.get(team_url)
       
#Team stats table
table = driver.find_element_by_class_name('nba-stat-table__overflow')

#Parsing thru team data
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

#Remove comment  if you want to save team_db to a csv file, add custom path
#team_db.to_csv(r'C:\projects\NBA\NBAstats.csv', index = False, header=True)

#Up to this point all leg work done, now do meaningful stuff with data

#Create user interaction

print('\nAll data was collected successfully!\n')
user_input = input('Would you like to continue? Enter y/n: ')

if(user_input == 'y' or user_input == 'yes' ):
	print('\nHere are some plots showing basic statistics\n')
	#Plot Team FGA vs. FG%
	fga_vs_per_plot = plt.figure(1)
	plt.scatter(team_db['FGA'],team_db['FG%'])
	plt.xlabel('Field Goals Attempted (per game)', fontsize=16, fontweight= 'bold')
	plt.ylabel('Field Goal % (per game)', fontsize=16, fontweight='bold')
	plt.xticks(fontsize=14, fontweight='bold')
	plt.yticks(fontsize=14, fontweight='bold')
	plt.xlim([80,95])
	plt.ylim([42, 50])

	#Plot Team FG% vs. Win or NBA standing
	per_vs_wins_plot = plt.figure(2)
	plt.scatter(team_db['FG%'],team_db['W'])
	plt.xlabel('Field Goals % (per game)', fontsize=16, fontweight= 'bold')
	plt.ylabel('Number of wins (per season)', fontsize=16, fontweight='bold')
	plt.xticks(fontsize=14, fontweight='bold')
	plt.yticks(fontsize=14, fontweight='bold')
	plt.xlim([42,50])
	plt.ylim([10, 82])
	plt.show()


	#Print panda dataframe
	print(team_db)

elif(user_input == 'n' or user_input == 'no'):
	print('Here is some data before you leave')
	print(team_db)
	print('\nGoodbye')
	exit()

else: #not yes or not so shutdown program
	print('Not a valid option, shutting down program')
	exit()