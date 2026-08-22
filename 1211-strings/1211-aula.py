while True:
    try:
        n = int(input())
    except EOFError:
        break

    telefones = []

    for _ in range(n):
        telefones.append(input().strip())

    telefones.sort()

    economia = 0

    for i in range(1, n):
        anterior = telefones[i - 1]
        atual = telefones[i]

        j = 0

        while j < len(atual) and atual[j] == anterior[j]:
            j += 1

        economia += j

    print(economia)