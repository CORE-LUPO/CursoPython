"""
DocString (usada geralmente para documentação de funções, classes ou arquivos)
Aqui também foi usada para explicar:
- Python é uma linguagem de programação
- Tipagem dinâmica (tipo muda conforme o valor) e forte (não converte tipo sem permissão)
- str = tipo string = texto
- Strings são textos entre aspas (simples ou duplas)
"""

print(1234)  # Número inteiro sendo impresso normalmente

# -------------------------
# Aspas simples
print('Luiz Otávio')  # String com aspas simples
print(1, 'Luiz "Otávio"')  # Dentro da string pode ter aspas duplas sem problema

# -------------------------
# Aspas duplas
print("Luiz Otávio")  # String com aspas duplas
print(2, "Luiz 'Otávio'")  # Dentro da string pode ter aspas simples sem problema

# -------------------------
# Escape com barra invertida (\) — permite inserir aspas dentro de aspas do mesmo tipo
print("Luiz \"Otávio\"")  # O caractere \" insere aspas duplas dentro da string

# --------------------------
# r = raw string (ignora o caractere de escape \)
print(r"Luiz \"Otávio\"")  # Aqui o Python imprime literalmente o texto, incluindo a barra invertida
