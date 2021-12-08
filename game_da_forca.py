
#============================= Base De Dados ==============================================================
Base_programacao = {
    'cobra' : 'python',
    'marcacao de hipertexto' : 'html',
    'estilo em cascata':'css',
    'programador completo':'fullstack',
    'engrenagem de paginas web' : 'javascript',    
}

Base_bibliotecas = {
    'analise e manipulacao de dados' : 'pandas',
    'ferramenta que constroi grafico com base nos dados' : 'matplotlib',
    'faz o processamento de matrizes e vetores' : 'numpy',
    'gera,altera,remove e converte datas e horarios' : 'arrow',
    ' soluções simples para mineração de dados (Data Mining) e extração de conhecimento (KDD - Knowledge Discovery in Data).' : 'pytil'
}

Base_builtInFunctions = {
    'recebe uma entrada de dados do usuário' : 'input',
    'retorna a soma dos valores de entrada da coluna ou expressão' : 'sum',
    'retorna a quantidade de elementos de qualquer lista ' : 'len',
    'retorna a quantidade de vezes que um mesmo elemento está contido numa lista' : 'count',
    'retorna a posição de determinado elemento' : 'index'
}
#============================= Base De Dados ==============================================================
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
