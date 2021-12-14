import baseDeDados
import random
import game
from game import *

def exibirRegras():
    print('\033[1;31;47m=\033[m' *15)    
    print('\033[1;31mREGRAS DO JOGO: \033[m')
    print('\033[1;31;47m=\033[m' *15)
    print('\033[0;31mregra nº1\033[m - Vocês terão que adivinhar letra por letra;')
    print('\033[0;31mregra nº2\033[m - São 5 tentativas por turno;')
    print('\033[0;31mregra nº3\033[m - Errou passa para o próximo jogador;')
    print('\033[0;31mregra nº4\033[m - Limite de acertos é do tamanho da palavra;')
    print('\033[0;31mregra nº5\033[m - O limite de jogadores serão de 3 players;') 
    print('\033[0;31mregra nº6\033[m - O jogo finalizará quando o primeiro jogador acertar uma palavra ou ao errar 5x.')



def jogar():
    print('=====' *10)
    print('================= JOGO DA FORCA ==================')
    print('=====' *10)
    
    var_multiplayer = multiplayer()
    player_index = 0
    losers_list = []
    multi_enforcou = False
    acertou = False

    regras = input('Quer ver as regras? ')
    if "sim" in regras:
      exibirRegras() 
      
    while(not multi_enforcou and not acertou):
      if player_index in losers_list:
        player_index+=1

      player = var_multiplayer.players_list[player_index]
      print(player.guess)
      
      chute = input(f'Digite uma letra, {player.name}: ')
      chute = chute.strip().upper()
      
      if(chute in player.word):

        index = 0
        for letra in player.word:
          if(chute == letra):
            player.set_guess(index, chute)
          index += 1
        acertou = '_' not in player.guess

      else:
        player.set_error()
        tentativas = 5-player.error

        if tentativas == 0:
          losers_list.append(player_index)
          print(f'Você perdeu {player.name}')

        print(f'Você errou! Faltam {tentativas} tentativas, {player.name} ')
        
        player_index += 1
        if player_index == len(var_multiplayer.players_list):
          player_index = 0
        
        soma = 0
        for x in var_multiplayer.players_list:
          soma += x.error
        multi_enforcou = soma == 5*len(var_multiplayer.players_list)


    if (acertou):
      print(player.guess)
      print(f'Você ganhou, {player.name}!!')
    else:
        print('Você perdeu!!')
    print('===== FIM =====')


if(__name__ == '__main__') :
    jogar()
