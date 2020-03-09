from elopy import Implementation


class League():
	def __init__(self, game, players_path):
		self.INITIAL_ELO = 1200

		self.game = Game(game)
		self.players = {}
		self._create_players()

		self.ranking = Ranking(self.players, initial_elo=self.INITIAL_ELO)



	def play_round(self):
		pairings = self._get_pairings()

	def _create_players(self, players_path):
		for alias, model in read_csv(players_path):
			self.players['alias'] = Player(alias, model_path)


	def _get_pairings(self):
		ordered = sorted(self.ranking.getRatingList(),
						 key = lambda test_list: test_list[1])
		pairs = []
		while len(ordered)>1:
		    o_ = ordered[:6]
		    idx = np.random.choice(range(min(5, len(ordered))), 2, replace=False)
		    p1 = o_[idx[0]]
		    p2 = o_[idx[1]]
		    pairs.append([p1, p2])
		    ordered.pop(ordered.index(p1))
		    ordered.pop(ordered.index(p2))

	def _update_ranking(self, info):
		pass

	def print_ranking(self):
		pass


class Player():
	def __init__(self, alias, model_path):
		self.alias = alias
		self.model = self._load_model()

	def _load_model(self, model_path):
		# load the model once
		pass

	def act(self, obs):
		self.model.act(obs)


class Match():
	def __init__(self, env_name, player_1, player_2):
		self.env = None # loadd env
		self.player_1 = player_1
		self.player_2 = player_2

	def _load_players(self, player):
		pass

	def play(self):
		self.env.reset()
		# game loop
		# last infor object returns the winnder of the game

		self.results = info

class Ranking():
	def __init__(self, players, initial_elo=1200):
		self.ranking = Implementation()

		for player in players.keys():
			self.ranking.addPlayer(player, rating=self.INITIAL_ELO)

		self.history = []

	def update_ranking(self, p1, p2, winner=None, draw=False):
		self.ranking.recordMatch(p1, p2, winner=winner, draw=draw)
		result = winner if winner is not None else 'draw'
		self.history.append((p1, p2, results))


	def print_ranking(self):
		for p in sorted(i.getRatingList(),
						key=lambda t: t[1], reverse=True):
			print(f'{p[0]} : {round(p[1])}')

