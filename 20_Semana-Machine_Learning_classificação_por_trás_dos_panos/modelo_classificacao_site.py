import csv

def carregar_acessos():
	dados = []     #Lado esquerdo x (o que sei as informações)
	marcacoes = [] #Lado direito y (o que não sei)

	arquivo = open('acesso.csv', 'rb')
	leitor = csv.reader(arquivo)
    
    #Ignorar primeira linha
    #leitor.next()
    
	for acessou_home, acessou_como_funciona, acessou_contato,
	    comprou in leitor:

        # INT para converter os itens de str para inteiro    
	    dados.append([int(acessou_home), 
            int(acessou_como_funciona), int(acessou_contato)])
	    marcacoes.append(int(comprou))
        
	return dados, marcacoes

# CHAMANDO ARQUIVO
# from dados import carregar_acessos
# dados, marcacoes = carregar_acessos()
# marcacoes