#Ele só lê o que tá no elemento de fora, não acessa o que tá dentro
lista=[["caio",["keven"]],'joão',["camila","fernando",["mama"]]]

for i in lista:
    for j in i:
        if "keven" in j:
            print ("Achou",i)
        else:
            print("Não achou",i)