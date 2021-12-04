

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