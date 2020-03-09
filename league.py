

class League():
	def __init__(self, game, players_path):
		self.game = Game(game)

	def create_ranking(self):
		pass

	def play_round(self):
		pairings = self._get_pairings()

		
	def _get_pairings(self):
		# from self.ranking	
		pass

	def _update_ranking(self):
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


