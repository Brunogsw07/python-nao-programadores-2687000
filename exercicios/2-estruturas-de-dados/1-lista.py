numerica = [1, 2, 3, 4, 5]
print(numerica)
mista = ['bruno', 2, 'guilherme', [1, 2, 3, 4]]
mista[0]
len(mista)
mista[3]
mista.append('note')
print(mista)
mista.extend(numerica)
print(mista)
len(mista)
mista[2]
mista[2] = 'wagner'
print(mista)
mista.remove('note')
print(mista)
mista[0:-1:2]
print(mista)

# Crie uma lista apenas com elementos numéricos
numericos = [0, 1, 2, 3, 4]
print(numericos)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
motogp = ['Marc', 93, 10.5, True, 'Rossi', 46, 8.5, False]
len(motogp)

# Imprima na tela apenas os 5 primeiros elementos da lista
motogp[:5]

# Crie um slice na lista para que imprima na tela os elementos de índice par
motogp[::2]

# Remova da lista o último item
motogp.remove(motogp[-1])
print(motogp)

# Insira na lista um novo item
motogp.append('Marquez')
print(motogp)
motogp.remove('Marquez')
print(motogp)

# Remova da lista um item específico
motogp.remove(10.5)
print(motogp)