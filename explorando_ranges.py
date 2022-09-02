"""
Ranges:

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utlizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

- Forma 1:
range(valor_de_parada)

Obs: valor_de_parada não inclusive(início padrão 0, e passo de 1 em 1)



#Forma 1:

for num in range(11):
    print(num)

#ele começou em zero e foi até 10, iniciando em 0 e terminando em 10.

# Forma 2:

for num in range(4, 11):
    print(num)

range(valor_de_inicio, valor_de_parada)
Obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)


#Forma 3:

for num in range(1, 10, 2):
    print(num)

range(valor_de_inicio, valor_de_parada, passo)
Obs: valor_de_parada não inclusive(início especificado pelo usuário, e passo específicado pelo usuário)


#Forma 4:(inversa)
range(valor_de_final, valor_de_parada, passo)
Obs: valor_de_parada não inclusives (valor_final especificado pelo usuário, e passo específico pelo usuário.)
"""

for num in range(10, 0, -1):
    print(num)
