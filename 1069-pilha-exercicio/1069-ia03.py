def resolver():
    num_casos = int(input().strip())

    for _ in range(num_casos):
        # 1. Higienização: descarta toda a areia ('.')
        mina = input().replace('.', '')
        diamantes = 0

        # 2. Redução iterativa: extrai pares '<>' adjacentes até estabilizar
        while '<>' in mina:
            diamantes += mina.count('<>')
            mina = mina.replace('<>', '')

        print(diamantes)

if __name__ == "__main__":
    resolver()