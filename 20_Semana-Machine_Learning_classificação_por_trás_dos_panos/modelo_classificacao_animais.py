#Descricao dos animais que conheço
#é gordinho?, tem perninha curta?, faz auau?

porco1 = [1, 1, 0]    #é gordinho, tem perna curta, não faz auau
porco2 = [1, 1, 0]    #é gordinho, tem perna curta, não faz auau
porco3 = [1, 1, 0]    #é gordinho, tem perna curta, não faz auau
cachorro1 = [1, 1, 1] #é gordinho, tem perna curta,faz auau
cachorro2 = [0, 1, 1] #não é gordinho, tem perna curta,faz auau
cachorro3 = [0, 1, 1] #não é gordinho, tem perna curta,faz auau

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes= [1,1,1,-1,-1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB() #Criando modelo
modelo.fit(dados, marcacoes) #Treinando modelo

#será um cachorro ou um porco
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
teste = [misterioso1, misterioso2]
print(modelo.predict(teste))