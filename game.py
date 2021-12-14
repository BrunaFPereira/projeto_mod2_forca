class Player:
  guess = []
  error = 0
  def __init__(self, name, word):
    self.name = name
    self.word = word
    self.guess = ['_' for x in word]
  
  def set_error(self):
    self.error+=1
  
  def get_error(self):
    return self.error

  def get_word(self):
    return self.word

  def set_guess(self, i, letter):
    self.guess[i] = letter

  def get_guess(self):
    return self.guess

class Multiplayer:
  def __init__(self, players_list):
    self.players_list = players_list

def multiplayer():
  player_list = []

  players_quantity_str = input('Type how many players will be playing: ')
  players_quantity_int = int(players_quantity_str)
  word = base_choice(players_quantity_int)
  
  for i, j in enumerate(word):
    nome = input(f'Type the name of player {i+1}: ')
    objPlayer = Player(nome, j.upper())
    player_list.append(objPlayer)

  objMultiplayer = Multiplayer(player_list)

  return objMultiplayer

def base_choice(number_of_players):
  # base choice
  base_programacao = ['python', 'html', 'javascript', 'fullstack', 'css']

  base_bibliotecas = ['pandas', 'matplotlib', 'numpy', 'arrow', 'datetime', 'scikitlearning', 'arrow', 'pytil']

  base_inteligencia_emocional = ['autoconhecimento', 'autocontrole', 'empatia', 'automotivação', 'empatia', 'relacionamento interpessoal']

  base = input('Escolha o tema\n1 - Programacao\n2 - Bibliotecas\n3 - Inteligencia Emocional\n')
  # word choice

  if int(base) == 1:
    return random_choice(base_programacao, number_of_players)

  elif int(base)==2:
    return random_choice(base_bibliotecas, number_of_players)

  else:
    return random_choice(base_inteligencia_emocional, number_of_players)
  
def random_choice(words_base, number_of_players):
  random.seed(8)
  words_list = []
  numeros = random.getstate()
  a = random.sample(range(len(words_base)), k = number_of_players)
  for x in a:
    words_list.append(words_base[x])
  return words_list

