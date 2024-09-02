def base_para_decimal(numero, base_origem):
    """
    Converte um número de uma base qualquer para a base decimal (base 10)
    """
    numero = str(numero).split('.')
    digitos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valor_decimal = 0

    # Parte inteira
    parte_inteira = numero[0]
    print(f"Convertendo parte inteira '{parte_inteira}' da base {base_origem} para decimal:")
    for i, digito in enumerate(parte_inteira[::-1]):
        valor = digitos.index(digito.upper())
        if valor >= base_origem:
            raise ValueError(f"Dígito {digito} não é válido na base {base_origem}.")
        valor_decimal += valor * (base_origem ** i)
        print(f"  {digito} (valor {valor}) * ({base_origem} ** {i}) = {valor * (base_origem ** i)}")

    # Parte fracionária
    if len(numero) > 1:
        parte_fracionaria = numero[1]
        print(f"Convertendo parte fracionária '{parte_fracionaria}' da base {base_origem} para decimal:")
        for i, digito in enumerate(parte_fracionaria):
            valor = digitos.index(digito.upper())
            if valor >= base_origem:
                raise ValueError(f"Dígito {digito} não é válido na base {base_origem}.")
            valor_decimal += valor * (base_origem ** -(i + 1))
            print(f"  {digito} (valor {valor}) * ({base_origem} ** -({i + 1})) = {valor * (base_origem ** -(i + 1))}")

    return valor_decimal

def decimal_para_base(numero, base):
    """
    Converte um número decimal para qualquer outra base (base_destino)
    """
    if numero == 0:
        return "0"
    
    # Parte inteira
    parte_inteira = int(numero)
    restos = []
    print(f"Convertendo parte inteira {parte_inteira} para base {base}:")
    while parte_inteira > 0:
        resto = parte_inteira % base
        restos.append(resto)
        print(f"{parte_inteira} / {base} = {parte_inteira // base}      Resto: {resto}")
        parte_inteira //= base

    digitos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    convertido_inteiro = ''.join(digitos[resto] for resto in restos[::-1])

    # Parte fracionária
    parte_fracionaria = numero - int(numero)
    convertido_fracionário = ''
    print(f"Convertendo parte fracionária {parte_fracionaria} para base {base}:")
    while parte_fracionaria > 0 and len(convertido_fracionário) < 4:
        parte_fracionaria *= base
        digito = int(parte_fracionaria)
        convertido_fracionário += digitos[digito]
        print(f"  {parte_fracionaria} * {base} = {parte_fracionaria}, dígito {digito}")
        parte_fracionaria -= digito

    if convertido_fracionário:
        return f"{convertido_inteiro}.{convertido_fracionário}"
    else:
        return convertido_inteiro

def converter_bases(numero, base_origem, base_destino):
    """
    Converte um número de uma base_origem para uma base_destino.
    """
    numero_decimal = base_para_decimal(numero, base_origem)
    return decimal_para_base(numero_decimal, base_destino)

numero = input("Digite um número para converter: ")
base_origem = int(input("Digite a base do número fornecido (2-36): "))
base_destino = int(input("Digite a base de destino (2-36): "))

if base_origem < 2 or base_origem > 36 or base_destino < 2 or base_destino > 36:
    print("Bases inválidas! Por favor, insira bases entre 2 e 36.")
else:
    try:
        resultado = converter_bases(numero, base_origem, base_destino)
        print(f"O número {numero} da base {base_origem} na base {base_destino} é: {resultado}")
    except ValueError as e:
        print(e)
