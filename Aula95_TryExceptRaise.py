def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')  # 🚨 Lança erro com mensagem personalizada
    return True  # 👍 Retorna True se não for zero


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):  # 🧪 Verifica se n é do tipo float ou int
        raise TypeError(                  # 🚨 Se não for, lança erro com info do tipo errado
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True  # 👍 OK se for número


def divide(n, d):
    deve_ser_int_ou_float(n)  # ✅ Valida o numerador
    deve_ser_int_ou_float(d)  # ✅ Valida o denominador
    nao_aceito_zero(d)        # 🚫 Se for zero, levanta erro
    return n / d              # ✅ Divide normalmente


print(divide(8, '0'))  # ❌ Aqui vai gerar um TypeError, pois '0' é uma string
