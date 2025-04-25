adicao = 10 + 10                      # soma: 10 + 10 = 20
print('Adição', adicao)              # imprime: Adição 20

subtracao = 10 - 5                   # subtração: 10 - 5 = 5
print('Subtração', subtracao)        # imprime: Subtração 5

multiplicacao = 10 * 10             # multiplicação: 10 vezes 10 = 100
print('Multiplicação', multiplicacao)  # imprime: Multiplicação 100

divisao = 10 / 3                    # divisão comum: resultado com ponto flutuante ≈ 3.333...
print('Divisão', divisao)           # imprime: Divisão 3.333...

divisao_inteira = 10 // 3           # divisão inteira: ignora a parte decimal → 3
print('Divisão inteira', divisao_inteira)  # imprime: Divisão inteira 3

exponenciacao = 2 ** 10             # exponenciação: 2 elevado a 10 → 1024
print('Exponenciação', exponenciacao)  # imprime: Exponenciação 1024

modulo = 55 % 2                     # módulo: resto da divisão de 55 por 2 → 1 (ímpar)
print('Módulo', modulo)             # imprime: Módulo 1

# Testes de divisibilidade usando o operador %
print(10 % 8 == 0)  # False → 10 ÷ 8 sobra 2
print(16 % 8 == 0)  # True  → 16 ÷ 8 sobra 0 (é divisível)
print(10 % 2 == 0)  # True  → 10 ÷ 2 sobra 0 (é par)
print(15 % 2 == 0)  # False → 15 ÷ 2 sobra 1 (ímpar)
print(16 % 2 == 0)  # True  → 16 ÷ 2 sobra 0 (par)
