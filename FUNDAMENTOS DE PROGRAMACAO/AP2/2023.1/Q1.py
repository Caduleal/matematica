import struct 

conversoes = struct.Struct("20s 20s f")
printInfo = False

def decodifica_dados_conversao(bloco):
    campos = conversoes.unpack(bloco)

    moeda1 = campos[0].decode('utf-8').strip(chr(0))
    moeda2 = campos[1].decode('utf-8').strip(chr(0)).strip('\n')
    taxa = campos[2]
    return moeda1, moeda2, taxa

def eh_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def processar_arquivo_conversoes(nome_arquivo_conversao, tipo1,tipo2,valor):
    dic = {'real': 'BRL','dolar':'USD','euro':'EUR'}
    with open(nome_arquivo_conversao, 'rb') as arquivo:
        while True:
            bloco = arquivo.read(conversoes.size)
            if not bloco:
                break
            moeda1,moeda2,taxa = decodifica_dados_conversao(bloco)
            if tipo1 == moeda1:
                if tipo2 == moeda2:
                    total = float(taxa)*float(valor)
                    total = float(f"{total:.2f}")
                    print(f"Voce pagará {total} {dic[moeda2]} por {valor} {dic[moeda1]}")
                    