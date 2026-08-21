casos = int(input())

for _ in range(casos):
    n = int(input())

    vagoes = list(map(int, input().split()))

    trocas = 0

    for i in range(1, n):

        j = i

        while j > 0 and vagoes[j] < vagoes[j - 1]:

            vagoes[j], vagoes[j - 1] = vagoes[j - 1], vagoes[j]

            trocas += 1

            j -= 1

    print(f"Optimal train swapping takes {trocas} swaps.")