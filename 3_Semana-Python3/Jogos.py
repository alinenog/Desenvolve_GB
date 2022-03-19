# Importando os dois jogos externos
import forca
import adivinhacao


def escolher_jogo():
    print('=-'*19)
    print('      COLETÂNIA DE JOGOS     ')
    print('=-'*19)

    print('''
        [1] Jogo da Forca
        [2] Jogo da adivinhação
    ''')
    opcao = int(input('Qual jogo você quer jogar? \n'))

    if opcao == 1:
        print('Bora Jogar... Jogo da Forca!')
        # chamando a função forca
        forca.jogar_forca()
    elif opcao == 2:
        print('Bora Jogar... \n Jogo da Adivinhação!')
        # chamando a função adivinhação
        adivinhacao.jogar_adivinhacao()
    else:
        print('Erro... \n Escolha a opção 1 ou 2.')


if (__name__ == "__main__"):
    escolher_jogo
