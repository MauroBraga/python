minhaLista = ["abacaxi", "melancia", "abacate"]
minhaLista2 = [1,2,3]
minhaLista3 = ["abacaxi",2, 9.89, True] 

print(minhaLista)
print(minhaLista2)
print(minhaLista3)

print(minhaLista[0])

for item in minhaLista:
    print(item)

print(len(minhaLista))

minhaLista.append("flamengo")

print(minhaLista)

del minhaLista[2:]
print(minhaLista)

minhaLista4 = []
minhaLista4.append(57)
print(minhaLista4)