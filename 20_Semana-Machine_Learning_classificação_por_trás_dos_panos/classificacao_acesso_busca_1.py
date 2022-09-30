#Sem o pandas

import csv

#Criando a função
def carregar_acessos()

    X = []
    Y = []

    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)

    leitor.next() #Ignora a primeira linha

    for home,planos_de_cursos,contato,comprou in leitor

        dado = ([int(home),int(planos_de_cursos)
            ,int(contato)])
        X.append(dado)
        Y.append(int(comprou))

    return X, Y

#Chamando codigo
#from dados import carregar_buscas
#x, y =  carregar_buscas()
#print(x)