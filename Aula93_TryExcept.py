try:
    a = 18
    b = 0
    # print(b[0])                # Essa linha está comentada, então não será executada
    print('Linha 1'[1000])       # ❌ Vai gerar um **IndexError**
    c = a / b                    # ❌ Seria um **ZeroDivisionError**, mas não será executada
    print('Linha 2')             # ❌ Não será executada porque a exceção acima para o fluxo
except ZeroDivisionError:
    print('Dividiu por zero.')   # Não entra aqui, pois o erro que ocorreu foi outro
except NameError:
    print('Nome b não está definido')  # Também não entra
except (TypeError, IndexError):
    print('TypeError + IndexError')  # ✅ Vai cair aqui por causa do IndexError
except Exception:
    print('ERRO DESCONHECIDO.')  # Só entraria aqui se fosse uma exceção não tratada acima

print('CONTINUAR')               # ✅ Sempre será executado, pois está fora do bloco try/except

