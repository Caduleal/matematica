def inverter_linhas_arquivo(nome_entrada, nome_saida):
    with open(nome_entrada, 'r', encoding="utf-8") as f:
        posicoes = []
        while True:
            pos = f.tell()
            linha = f.readline()
            if not linha:
                break
            posicoes.append(pos)
        
    with open(nome_entrada, 'r', encoding='utf-8') as f_in, open(nome_saida,'w',encoding='utf-8') as f_out:
        for pos in reversed(posicoes):
            f_in.seek(pos)
            f_out.write(f_in.readline())

def main():
    nome_entrada = input("Digite o nome do arquivo de entrada: ")
    nome_saida = "Saida_invertida.txt"
    inverter_linhas_arquivo(nome_entrada, nome_saida)
    print(f"Arquivo de saida gerado: {nome_saida}")

#Teste - exemplo1.txt
main()
