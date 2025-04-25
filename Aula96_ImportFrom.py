# Módulos padrão do Python (import, from, as e *)

# 🔗 Link oficial com todos os módulos padrão do Python:
# https://docs.python.org/3/py-modindex.html

# --- EXEMPLO 1: importando o módulo inteiro ---
import sys  # importa o módulo inteiro 'sys'

platform = 'A MINHA'  # variável local com o mesmo nome de um atributo do módulo sys

print(sys.platform)  # imprime a plataforma do sistema (ex: 'win32', 'linux', etc.)
print(platform)  # imprime a string local 'A MINHA'

# ✅ Vantagem: Evita conflito de nomes, pois tudo vem com o namespace (sys.)
# ❌ Desvantagem: Fica mais longo de digitar (sys.platform, sys.exit...)

# --- EXEMPLO 2: importando partes do módulo ---
from sys import exit, platform  # importa apenas os objetos 'exit' e 'platform'

print(platform)  # imprime diretamente o platform do sistema, sem sys.

# ✅ Vantagem: Código mais curto
# ❌ Desvantagem: Pode haver conflito de nomes com variáveis locais

# --- EXEMPLO 3: usando alias para o módulo inteiro ---
import sys as s  # importa o módulo sys e dá o apelido 's'

sys = 'alguma coisa'  # cria uma variável local chamada 'sys' (isso NÃO afeta o apelido 's')

print(s.platform)  # acessa corretamente o atributo do módulo usando o apelido
print(sys)  # imprime a string 'alguma coisa'

# ✅ Vantagem: Evita conflitos e economiza digitação
# ❌ Desvantagem: Se o apelido for ruim/confuso, atrapalha leitura

# --- EXEMPLO 4: usando alias para objetos individuais ---
from sys import exit as ex  # importa 'exit' com apelido 'ex'
from sys import platform as pf  # importa 'platform' com apelido 'pf'

print(pf)  # imprime a plataforma usando o apelido

# ✅ Vantagem: Você pode evitar conflito e customizar os nomes
# ❌ Desvantagem: Pode fugir do padrão e deixar o código menos claro

# --- EXEMPLO 5: importando tudo do módulo (má prática) ---
# from sys import *  # (⚠️ Evite isso)

# print(platform)  # funciona, mas não é claro de onde vem 'platform'
# exit()  # encerra o programa

# ✅ Vantagem: Prático (tudo disponível direto)
# ❌ Desvantagem: Polui o namespace e causa confusão (você não sabe de onde veio cada nome)
