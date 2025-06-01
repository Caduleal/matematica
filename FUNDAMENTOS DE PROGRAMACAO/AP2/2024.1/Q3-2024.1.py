import struct
Frete = struct.Struct("8s 5s f") #Como o arquivo está DIVIDIDO 8 caracteres string, 5 caracteres de string e float

def decodificar_dados_frete(bloco):
    campos = Frete.unpack(bloco)
    cep = campos[0].decode("utf-8")
    nomeLoja = campos[1].decode("utf-8").rstrip(chr(0))
    valor_frete = round(campos[2],2)
    return cep, nomeLoja, valor_frete

def processa_arquivo_frete_bin(arquivo_frete,cep_destinatario):
    frete = dict()
    with open(arquivo_frete, "rb") as arquivo:
        while (True):
            bloco = arquivo.read(Frete.size)
            if (not bloco):
                break
            cep, nome_loja, valor_frete = decodificar_dados_frete(bloco)

            if (cep==cep_destinatario):
                frete[nome_loja] = valor_frete
    return frete

def get_melhor_custo(arquivo_produto, frete):
    melhor_custo= {"nome_produto": None, "nome_loja":None,"custo_total":None}

    if(not frete):
        return None
    
    with open(arquivo_produto,'r') as arquivo:
        melhor_custo["nome_produto"] = arquivo.readline().strip("\n")
        for linha in arquivo:
            dados= linha.split()
            if (len(dados)>1):
                nome_loja = dados[0]
                valor_produto = float(dados[1])

                custo_total = valor_produto+frete[nome_loja]
                if(melhor_custo["nome_loja"]==None or custo_total < melhor_custo["custo_total"]):
                    melhor_custo["nome_loja"] = nome_loja
                    melhor_custo["custo_total"] = custo_total
    return melhor_custo

def main():
    nome_arquivo_frete= input()
    nome_arquivo_produto = input()
    cep_destinatario = input().replace(".","").replace("-",'')

    try:
        frete = processa_arquivo_frete_bin(nome_arquivo_frete,cep_destinatario)
        melhor_custo = get_melhor_custo(nome_arquivo_produto, frete)
        msg=""
        if(not frete):
            msg="O produto desejado não pode ser entregue neste frete"
        else:
            msg = "A melhor loja do "+ melhor_custo["nome_produto"]
            sg = "A melhor loja do " + melhor_custo["nome_produto"] + " para o CEP " + cep_destinatario + " é a "
            msg += melhor_custo["nome_loja"] + " com valor total de R$ " + "{:.2f}".format(melhor_custo["custo_total"]) + "."
        print(msg)
    except IOError:
        print('Um dos arquivos não foi encontrado.')
    return None
main()
