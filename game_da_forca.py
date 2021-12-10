import baseDeDados

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


print("teste")


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
