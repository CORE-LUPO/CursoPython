# \r\n -> CRLF (Carriage Return + Line Feed) → Quebra de linha usada no Windows
# \n -> LF (Line Feed) → Quebra de linha usada no Linux/macOS

# A função print() imprime os valores separados por 'sep' e termina com 'end'

print(12, 34, 1011, sep="", end='#')  # sep="" junta tudo SEM espaço, end="#" finaliza com '#'
# Saída: 12341011#

print(56, 78, sep='-', end='\n')  # sep='-' coloca hífen entre os valores, end='\n' quebra a linha
# Saída: 56-78

print(9, 10, sep='-', end='\n')  # mesmo comportamento acima
# Saída: 9-10
