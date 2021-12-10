import baseDeDados


def multiplayer():
  player_dict = {}

  players_quantity_str = input('Type how many players will be playing: ')
  chances = int(players_quantity_str)

  for player in range(1, chances+1):
    player_dict.update({'player_'+str(player):'5'})
  return player_dict

print(multiplayer())

#============================= Word Checker  ==============================================================
resposta = input('Digite a resposta: ')
if baseDeDados.Base_programacao['cobra'].find(resposta) != -1:
    print('acertou')
elif baseDeDados.Base_programacao['marcacao de hipertexto'].find(resposta) != -1:
    print('acertou')
elif baseDeDados.Base_programacao['estilo em cascata'].find(resposta) != -1:
    print('acertou')
elif baseDeDados.Base_programacao['programador completo'].find(resposta) != -1:
    print('acertou')
elif baseDeDados.Base_programacao['engrenagem de paginas web'].find(resposta) != -1:
    print('acertou')
else:
    print('errou!')

resposta = input('Digite a resposta: ')
if baseDeDados.Base_bibliotecas['analise e manipulacao de dados'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_bibliotecas['ferramenta que constroi grafico com base nos dados'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_bibliotecas['faz o processamento de matrizes e vetores'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_bibliotecas['gera,altera,remove e converte datas e horarios'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_bibliotecas['soluções simples para mineração de dados (Data Mining) e extração de conhecimento (KDD - Knowledge Discovery in Data).'].find(resposta) != -1:
     print('acertou')
else:
    print('errou!')  

resposta = input ('Digite a resposta: ')
if baseDeDados.Base_builtInFunctions['recebe uma entrada de dados do usuário'].find(resposta) != -1:
    print('acertou ')
elif baseDeDados.Base_builtInFunctions['retorna a soma dos valores de entrada da coluna ou expressão'].find(resposta)!= -1:
    print ('acertou')
elif baseDeDados.Base_builtInFunctions['retorna a quantidade de elementos de qualquer lista'].find(resposta) != -1:
    print ('acertou')
elif baseDeDados.Base_builtInFunctions['retorna a quantidade de vezes que um mesmo elemento está contido numa lista'].find(resposta)!= -1:
    print ('acertou')
elif baseDeDados.Base_builtInFunctions['retorna a posição de determinado elemento'].find(resposta)!= -1:
    print ('acertou')
else :
    print ('errou!')




resposta = input('Digite a resposta: ')
if baseDeDados.Base_pilares_inteligencia_e['habilidade de reconhecer suas proprias emocoes'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_pilares_inteligencia_e['habilidade controlar e redirecionar impulsos'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_pilares_inteligencia_e['habilidade de se manter motivado'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_pilares_inteligencia_e['habilidade de reconhecer e entender emocoes dos outros'].find(resposta) != -1:
     print('acertou')
elif baseDeDados.Base_pilares_inteligencia_e['habilidade desenvolver relacionamentos interpessoais'].find(resposta) != -1:
     print('acertou')
else:
    print('errou')


#============================= Word Checker ==============================================================


#============================= Word Checker  ==============================================================
resposta = input('Digite a resposta: ')
if Base_programacao['cobra'].find(resposta) != -1:
    print('acertou')
elif Base_programacao['marcacao de hipertexto'].find(resposta) != -1:
    print('acertou')
elif Base_programacao['estilo em cascata'].find(resposta) != -1:
    print('acertou')
elif Base_programacao['programador completo'].find(resposta) != -1:
    print('acertou')
elif Base_programacao['engrenagem de paginas web'].find(resposta) != -1:
    print('acertou')
else:
    print('errou!')
#Base_Programação.
        
def jogar():
    print('=====' *10)
    print('================= JOGO DA FORCA ==================')
    print('=====' *10)

    palavra_secreta = 'siriguela'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
       
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print(f'você errou! Faltam {5-tentativas} tentativas ')
        
        enforcou = tentativas == 5
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')
    print('===== FIM =====')


if(__name__ == '__main__') :
    jogar()
