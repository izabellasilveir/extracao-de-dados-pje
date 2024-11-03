import random

# Nome do arquivo de texto
nome_arquivo = "numeros_validos.txt"    

def gerar_numero_cnj():
    def bcmod(x, y):
        take = 5
        mod = ''

        while x:
            a = int(mod + x[:take])
            x = x[take:]
            mod = str(a % y)

        return mod

    # Gera um número sequencial aleatório (7)
    numero_sequencial = str(random.randint(0, 9999999)).zfill(7)
    
    # Gera o ano entre 2010 e 2023
    ano_ajuizamento = str(random.randint(2010, 2023))
    
    jtr = "8"
    tribunal = "06"
    foro = "0001"
    
    # Combina todas as partes em um número CNJ válido
    numero_base = f"{numero_sequencial}"
    
    digito_verificador = 98 - int(bcmod(numero_sequencial + ano_ajuizamento + jtr + tribunal + foro + '00', 97))

    numero_CNJ = f"{numero_base}-{digito_verificador}.{ano_ajuizamento}.{jtr}.{tribunal}.{foro}"
    
    # Número do processo sem o 8.06.0001
    numero_CNJ_formatted = f"{numero_base}-{digito_verificador}.{ano_ajuizamento}"

    return numero_CNJ_formatted
    