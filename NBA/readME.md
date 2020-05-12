# CPE 551 - NBA Stats

- This repo will contain the code for my CPE 551 - Engineering Programming Python final project. This python 
script uses [Selenium](https://selenium-python.readthedocs.io/) to scrap team statistics from the [2019-20 NBA season](https://stats.nba.com/teams/traditional/)

## NBA Stats - Python Final Project

### Requirements

- Install packages :  

```
pip install selenium 
pip install pandas
pip install numpy
pip install matplotlib
```

- Install Python 2.7 Interpreter

- Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), download the version the __matches__ your version of Chrome
	- Save the path of `chromedriver.exe` to your favorite text editor

### NBA Team Data

- Some of the team data collected include:
	- Games played
	- Wins
	- Losses
	- Win percentage
	- Minutes
	- Points
	- Field goals made
	- Field goals attepted
	- Field goal percentage

- Please refer to [NBAstats.csv](https://github.com/michaeldelcid/projects/blob/master/NBA/NBAstats.csv) to view all team data

### Run

- Enter the following commads:

`python NBAstats.py '<ChromeDriver file path>' `

- E.g. to run the script on my machine I type:

`python NBAstats.py 'C:\Eclipse\chromedriver.exe' `

- It is __EXTREMELY__ important that when you run the script, to wait until the following messages show up on your command prompt:

- In line 70 of `NBAstats.py` you have the option of saving the data to a CSV file, uncomment if you want to do this and enter a path

```
All data was collected successfully!

Would you like to continue? Enter y/n:
 ```

- By waiting I mean don't even think about interacting with Chrome browser when it opens, it causes weird errors
	- This has to do with how Selenium interacts with the webdriver
	- Even minimizing the web browser while data is being collected causes weird errors

### Future 

- I want to be able to collect data from ANY year and plot a teams performance over the years using different stats

- I included `nba_dictionary' to be able to look up a team name using its abbreviation and vice-versa
	- I want to enter 'New York Knicks' or 'NYK' and get data based on that team and plot it
	- At the moment it is plotting data for ALL 30 NBA teams

- I want to port all the player data into a csv BUT the method .find_element_by_xpath() is not working correctly for me
	- `player_data.py` was created for this purpose but it is buggy 

- I want to create a GUI that generate reports for a given team