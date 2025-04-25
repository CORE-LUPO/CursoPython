# Generator gen1 produz 3 valores: 1, 2, 3
def gen1():
    print('COMECOU GEN1')  # Mensagem de início
    yield 1  # Pausa aqui e entrega 1
    yield 2  # Depois entrega 2
    yield 3  # Depois entrega 3
    print('ACABOU GEN1')  # Só exibe isso quando o generator terminar

# Outro generator gen3 com valores diferentes
def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

# gen2 é um generator que pode usar outro generator dentro dele
def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen  # 'Delegação': entrega todos os valores do generator passado
    yield 4  # Continua com seus próprios valores
    yield 5
    yield 6
    print('ACABOU GEN2')

# Criando 3 generators diferentes com base no gen2
g1 = gen2(gen1())  # gen2 vai delegar os valores de gen1 primeiro, depois os seus
g2 = gen2(gen3())  # mesma lógica com gen3
g3 = gen2()        # sem generator extra, então só gera 4, 5, 6

# Iterando sobre g1 (vai mostrar gen1 + gen2)
for numero in g1:
    print(numero)
print()

# Iterando sobre g2 (gen3 + gen2)
for numero in g2:
    print(numero)
print()

# Iterando sobre g3 (só gen2, sem delegação)
for numero in g3:
    print(numero)
print()
