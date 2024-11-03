def validar_numero_unico_processo(numero):
    def bcmod(x, y):
        take = 5
        mod = ''

        while x:
            a = int(mod + x[:take])
            x = x[take:]
            mod = str(a % y)

        return mod

    numero_processo = numero.replace(".", "").replace("-", "")

    if len(numero_processo) < 14 or not numero_processo.isdigit():
        return False

    digito_verificador_extraido = int(numero_processo[-13:-11])

    vara = numero_processo[-4:]  # (4) vara originária do processo
    tribunal = numero_processo[-6:-4]  # (2) tribunal
    ramo = numero_processo[-7:-6]  # (1) ramo da justiça
    ano_inicio = numero_processo[-11:-7]  # (4) ano de inicio do processo
    tamanho = len(numero_processo) - 13
    numero_sequencial = numero_processo[:tamanho].zfill(7)  # (7) numero sequencial dado pela vara ou juizo de origem

    digito_verificador_calculado = 98 - int(bcmod(numero_sequencial + ano_inicio + ramo + tribunal + vara + '00', 97))

    print(digito_verificador_extraido)
    print(digito_verificador_calculado)
    return digito_verificador_extraido == digito_verificador_calculado

# Exemplo de uso:
numero = "0913083-13.2023.8.06.0001"
print(validar_numero_unico_processo(numero))