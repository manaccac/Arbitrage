from difflib import SequenceMatcher


mismatch_pairs = [
	["MelbourneCity", "MelbourneVictory"],
	["MelbourneCityFC", "MelbourneVictoryFC"]
]

def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()

def get_game(game, others):
	if (len(others) == 0 or game == None):
		return None
	m = 0
	m_obj = None
	for other in others:
		sim = str_similarity(game['team1'], other['team1']) + str_similarity(game['team2'], other['team2'])
		if (sim > m):
			m = sim
			m_obj = other
	if (str_similarity(game['team1'], m_obj['team1']) < 0.55):
		print("hello1")
		print(str_similarity(game['team1'], m_obj['team1']))
		print(game['team1'], " || " ,m_obj['team1'])
		return None
	if (str_similarity(game['team2'], m_obj['team2']) < 0.55):
		print("hello2")
		print(str_similarity(game['team2'], m_obj['team2']))
		print(game['team2'], " || " ,m_obj['team2'])
		return None
	for mismatch in mismatch_pairs:
		if ([game['team1'], m_obj['team1']] == mismatch or [m_obj['team1'], game['team1']] == mismatch):
			return None
		if ([game['team2'], m_obj['team2']] == mismatch or [m_obj['team2'], game['team2']] == mismatch):
			return None
	return m_obj

def arb3(a, n, b):
	return (1 - (1/a + 1/n + 1/b)) * 100

def arb2(a, b):
	return (1 - (1/a + 1/b)) * 100

def dec_to_base(num, base):
	base_num = ""
	while (num > 0):
		dig = int(num % base)
		if (dig < 10):
			base_num += str(dig)
		else:
			base_num += chr(ord('A')+dig-10)
		num //= base
	base_num = base_num[::-1]
	return base_num

def arb_football(games):
	nb_bookmakers = len(games)
	combinations = nb_bookmakers ** 3

	for game in games:
		try:
			print("{:10}: {} - {} @{}/{}/{}".format(game, games[game]['team1'], games[game]['team2'], games[game]['odds'][0], games[game]['odds'][1], games[game]['odds'][2]))
		except:
			continue
	for i in range(combinations):
		try:
			combination = str(dec_to_base(i, nb_bookmakers)).zfill(3)
			b1 = list(games.keys())[int(combination[0])]
			b2 = list(games.keys())[int(combination[1])]
			b3 = list(games.keys())[int(combination[2])]
			profit = arb3(
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
			)
			if (profit > 0):
				stakes = get_stakes3(
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
					10)
				print("Abritrage found for **{}**-**{}** with **{}/{}/{}** with odds {}/{}/{}: {:.2f}%".format(
					games[b1]['team1'],
					games[b1]['team2'],
					b1,
					b2,
					b3,
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
					profit
				))
				print("> Stakes: **{}**@{} on {} for A, **{}**@{} on {} for N, **{}**@{} on {} for B".format(
					stakes['rounded'][0],
					games[b1]['odds'][0],
					b1,
					stakes['rounded'][1],
					games[b2]['odds'][1],
					b2,
					stakes['rounded'][2],
					games[b3]['odds'][2],
					b3,
				))
			print("{}: ({:10}/{:10}/{:10}) {:.2f}%".format(
				" ".join(combination.split()),
				b1,
				b2,
				b3,
				profit
			))
		except:
			continue

def arb_basketball(games):
	nb_bookmakers = len(games)
	combinations = nb_bookmakers ** 2
	print("-- Arbitrage on: ")
	for game in games:
		# try:
			print("{:10}: {} - {} @{}/{}".format(game, games[game]['team1'], games[game]['team2'], games[game]['odds'][0], games[game]['odds'][1]))
		# except:
		# 	continue
	print("{} combinations possible --".format(combinations))
	for i in range(combinations):
		combination = str(dec_to_base(i, nb_bookmakers)).zfill(2)
		b1 = list(games.keys())[int(combination[0])]
		b2 = list(games.keys())[int(combination[1])]
		profit = arb2(
				games[b1]['odds'][0],
				games[b2]['odds'][1],
		)
		if (profit > 0):
			print("FOUND!!!!")
			stakes = get_stakes2(
				games[b1]['odds'][0],
				games[b2]['odds'][1],
				10)
			print("Abritrage found for **{}**-**{}** with **{}/{}** with odds {}/{}: {:.2f}%".format(
				games[b1]['team1'],
				games[b1]['team2'],
				b1,
				b2,
				games[b1]['odds'][0],
				games[b2]['odds'][1],
				profit
			))
			print("> Stakes: **{}**@{} on {} for A, **{}**@{} on {} for B".format(
				stakes['rounded'][0],
				games[b1]['odds'][0],
				b1,
				stakes['rounded'][1],
				games[b2]['odds'][1],
				b2
			))
		print("{}: ({:10}/{:10}) {:.2f}%".format(
			" ".join(combination.split()),
			b1,
			b2,
			profit
		))

def get_stakes3(a, n, b, investment):
	amount = arb3(a, n, b)
	tmp = (100 - amount) / 100
	return {
		'raw': (
			investment / (tmp * a),
			investment / (tmp * n),
			investment / (tmp * b)
		),
		'rounded': (
			round(investment / (tmp * a) * 10) / 10,
			round(investment / (tmp * n) * 10) / 10,
			round(investment / (tmp * b) * 10) / 10
		)
	}

def get_stakes2(a, b, investment):
	amount = arb2(a, b)
	tmp = (100 - amount) / 100
	return {
		'raw': (
			investment / (tmp * a),
			investment / (tmp * b)
		),
		'rounded': (
			round(investment / (tmp * a) * 10) / 10,
			round(investment / (tmp * b) * 10) / 10
		)
	}