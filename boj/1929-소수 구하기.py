def get_primes(m, n):
    sieve = [True] * (n+1)
    sieve[1] = False 
    k = int(n ** .5)
    
    for i in range(2, k+1):
        if sieve[i]:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [w for w in range(m, n+1) if sieve[w]]
 
M, N = map(int, input().split())
S = get_primes(M, N)
 
for s in S:
    print(s)