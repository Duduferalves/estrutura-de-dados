def resolver():
    try:
        entrada = input("Número de casos de teste: ").strip()
        if not entrada:
            return
        num_casos = int(entrada)
    except (EOFError, ValueError):
        return
    
    for _ in range(num_casos):
        linha = input("Linha de entrada: ")
        diamantes = 0
        abertos = 0
        
        for char in linha:
            if char == '<':
                abertos += 1
            elif char == '>' and abertos > 0:
                abertos -= 1
                diamantes += 1
                
        print(f"Quantidade de diamantes: {diamantes}")

if __name__ == "__main__":
    resolver()