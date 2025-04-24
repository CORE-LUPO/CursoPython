try:
    print('ABRIR ARQUIVO')     # Simula a abertura de um recurso (ex: arquivo, conexão etc.)
    8/0                        # ❌ Lança um ZeroDivisionError
except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Mostra o nome da exceção: 'ZeroDivisionError'
    print(e)                     # Mostra a mensagem do erro: 'division by zero'
    print('DIVIDIU ZERO')        # Mensagem personalizada
except IndexError as error:
    print('IndexError')          # Não será executado, pois o erro foi outro
except (NameError, ImportError):
    print('NameError, ImportError')  # Também não será executado
else:
    print('Não deu erro')        # ❌ Nunca entra aqui se tiver erro no try
finally:
    print('FECHAR ARQUIVO')      # ✅ SEMPRE executa, com ou sem erro

