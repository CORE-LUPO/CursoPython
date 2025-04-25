# Tipo de dado bool (boolean)
# Em programação, é fundamental entender que uma operação lógica pode resultar em duas respostas:
# Sim (True) ou Não (False), ambos são valores booleanos.

# O operador '==' verifica se dois valores são iguais
# Se forem iguais, a expressão retorna True (verdadeiro), senão retorna False (falso)

print(10 == 10)  # 10 é igual a 10? Sim => True (Verdadeiro)
print(10 == 11)  # 10 é igual a 11? Não => False (Falso)

# A função type() retorna o tipo do valor, então vamos ver o tipo de True, False, e o resultado de comparações:
print(type(True))  # True é do tipo booleano => <class 'bool'>
print(type(False)) # False também é do tipo booleano => <class 'bool'>
print(type(10 == 10))  # A expressão 10 == 10 retorna True => <class 'bool'>
print(type(10 == 11))  # A expressão 10 == 11 retorna False => <class 'bool'>
