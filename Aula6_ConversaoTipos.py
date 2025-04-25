# Conversão de tipos (coerção)
# Em Python, você pode converter um tipo de dado para outro usando funções específicas.

# Convertendo uma string '1' para inteiro
print(int('1'), type(int('1')))  # int('1') converte a string '1' para o inteiro 1 => <class 'int'>

# Convertendo o resultado de uma soma (float + int) para float
print(type(float('1') + 1))  # '1' vira float (1.0), e depois soma com 1, resultado é float => <class 'float'>

# Convertendo uma string para bool
# Uma string com pelo menos um caractere (como ' ') é considerada 'True' em Python
print(bool(' '))  # ' ' é uma string não vazia, logo é considerada True => True

# Convertendo o número inteiro 11 para string e concatenando com 'b'
print(str(11) + 'b')  # str(11) converte 11 para a string '11', depois concatena com 'b' => '11b'
