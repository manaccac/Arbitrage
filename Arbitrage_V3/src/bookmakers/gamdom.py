from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

competition_urls = {
	'football':
	{
		"ligue1": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/37",
		"liga": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/27",
		"bundesliga": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/26",
		"premier-league": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/11",
		"serie-a": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/25",
		"primeira": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/41",
		"serie-a-brasil": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/195",
		"a-league": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/68",
		"bundesliga-austria": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/70",
		"division-1a": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/44",
		"super-lig": "https://hub88b-ytuoyswg.betsy.gg/football/tournaments/32",
	},
	'basketball':
	{
		"nba": "https://hub88b-ytuoyswg.betsy.gg/basketball/tournaments/100",
		"euroleague": "https://hub88b-ytuoyswg.betsy.gg/basketball/tournaments/103",
	}
}

def get_games(competition):
	print("dans gamdom")
	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	s = Service('/usr/local/bin/chromedriver')	
	driver = webdriver.Chrome(service=s)
	driver.get("https://gamdom.com/sports")
	sleep(1)
	driver.get(url)
	sleep(4)
	i = len(driver.find_elements(By.CLASS_NAME, "grid-event__content"))

	j = 0
	count_name = 0
	count_odds = 0
	games = []
	while (j < i) :
		team1 = driver.find_elements(By.CLASS_NAME, "grid-event__competitor-name")[count_name].text
		team2 = driver.find_elements(By.CLASS_NAME, "grid-event__competitor-name")[count_name + 1].text
		odds = [
			float(driver.find_elements(By.CLASS_NAME, "_101")[count_odds].text.split("\n")[1]),
			float(driver.find_elements(By.CLASS_NAME, "_102")[count_odds].text.split("\n")[1]),
			float(driver.find_elements(By.CLASS_NAME, "_103")[count_odds].text.split("\n")[1])
			# outcome__number
		]

		# print(team1, team2)
		# print(odds)
		j = j + 1
		count_name = count_name + 2
		count_odds = count_odds + 1

		
		games.append({
			'team1': team1,
			'team2': team2,
			'odds': odds
		})

	return games
	