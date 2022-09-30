from dados import carregar_acessos

x, y = carregar_acessos()

#Separado 90% para treino e 10% para teste
treino_dados = x[:90]
treino_maracoes = y[:90]

#ultimas nove linhas
teste_dados = x[-9:]
teste_marcacoes = y[-9:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferencas =  resultado - teste_marcacoes 

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos/total de _elementos