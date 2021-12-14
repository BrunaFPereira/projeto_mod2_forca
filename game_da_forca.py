import baseDeDados
import random
import aux
        
def jogar():
    print('=====' *10)
    print('================= JOGO DA FORCA ==================')
    print('=====' *10)
    
    var_multiplayer = multiplayer()
    player_index = 0
    losers_list = []
    multi_enforcou = False
    acertou = False


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
