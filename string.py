a = "Mauro"
b = "Braga"

concat = a + " " + b + "\n"

tamanho = len(concat)

print(concat)

print(tamanho)

print(concat[2])

print(concat[0:5])

print(concat[0:])

print(concat.lower())

print(concat.upper())

print(concat.strip())

for i in concat.split(" "):
    print(i)

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split("r")
print(minha_lista)

busca = minha_string.find("rei")

print(busca)

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)