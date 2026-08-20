def resolver():
    num_casos = int(input().strip())

    for _ in range(num_casos):
        linha = input()
        pilha = []
        diamantes = 0

        for char in linha:
            if char == '<':
                pilha.append(char)  # Push: registra abertura
            elif char == '>':
                if pilha:
                    pilha.pop()     # Pop: fecha o par mais interno
                    diamantes += 1

        print(diamantes)

if __name__ == "__main__":
    resolver()