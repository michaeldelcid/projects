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

- Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads), download the version the _matches_ your version of Chrome
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

- Please refer to [NBAstats.csv](..blob/master/NBA/NBAstats.csv) to view all team data

### Run

- Enter the following commads:

`python NBAstats.py '<ChromeDriver file path>' `

- E.g. to run the script on my machine I type:

`python NBAstats.py 'C:\Eclipse\chromedriver.exe' `
 
