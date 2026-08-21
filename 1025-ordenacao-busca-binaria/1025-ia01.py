import sys

def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    caso = 1
    
    while True:
        try:
            n_str = next(iterator)
            q_str = next(iterator)
        except StopIteration:
            break
            
        N = int(n_str)
        Q = int(q_str)
        
        if N == 0 and Q == 0:
            break
            
        # O problema garante valores entre 0 e 10000
        MAX_VAL = 10000
        count = [0] * (MAX_VAL + 1)
        
        # 1. Contagem de frequência: O(N)
        for _ in range(N):
            val = int(next(iterator))
            count[val] += 1
            
        # 2. Pré-cálculo da primeira posição de cada valor: O(MAX_VAL)
        # first_pos[x] guardará o índice (1-based) onde o valor x aparece pela primeira vez
        first_pos = [-1] * (MAX_VAL + 1)
        current_index = 1
        
        for val in range(MAX_VAL + 1):
            if count[val] > 0:
                first_pos[val] = current_index
                current_index += count[val]
                
        # 3. Resposta imediata para cada query: O(1) por consulta
        print(f"CASE# {caso}:")
        for _ in range(Q):
            consulta = int(next(iterator))
            if consulta <= MAX_VAL and first_pos[consulta] != -1:
                print(f"{consulta} found at {first_pos[consulta]}")
            else:
                print(f"{consulta} not found")
                
        caso += 1

if __name__ == "__main__":
    resolver()
    
    
