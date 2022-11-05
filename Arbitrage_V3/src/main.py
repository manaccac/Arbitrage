import bookmakers.winamax as winamax
import bookmakers.pmu as pmu
import bookmakers.betclic as betclic
import bookmakers.zebet as zebet
import bookmakers.netbet as netbet
import bookmakers.gamdom as gamdom
import arb
import config
import traceback

# print(ps3838.get_games({'competition': 'nba', 'sport': 'basketball'}))
# exit(0)

progress = 0
for competition in config.competitions:
	progress += 1
	bookmakers = {}
	print("competition = ", competition)
	try:
		bookmakers['winamax'] = winamax.get_games(competition)
	except:
		print("erreur 1")
	try:
		bookmakers['pmu'] = pmu.get_games(competition)
	except:
		print("erreur 2")
	try:
		bookmakers['betclic'] = betclic.get_games(competition)
	except:
		print("erreur 3")
	try:
		bookmakers['zebet'] = zebet.get_games(competition)
	except:
		print("erreur 4")
	try:
		bookmakers['netbet'] = netbet.get_games(competition)
	except:
		print("erreur 5")
	try:
		bookmakers['gamdom'] = gamdom.get_games(competition)
	except:
		print("erreur 6")
	# break
	for game in bookmakers['winamax']:
		games = {}
		for bookmaker in bookmakers:
			try:
				g = arb.get_game(game, bookmakers[bookmaker])
				if (g):
					games[bookmaker] = g
			except:
				print("erreur")
		if (competition["sport"] == "football"):
			arb.arb_football(games)
		if (competition["sport"] == "basketball"):
			arb.arb_basketball(games)
	print("Progess: {:.2f}%".format(progress / len(config.competitions) * 100))