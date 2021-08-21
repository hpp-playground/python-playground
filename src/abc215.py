def factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def main():
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    primes = [True]*(M+1)
    primes[0] = False
    for a in A:
        factors = factorize(a)
        for fi in factors:
            if fi > M: continue
            if primes[fi]:
                tmp = fi
                while tmp <= M:
                    primes[tmp] = False
                    tmp += fi
    print(sum(primes))
    for prime, flag in enumerate(primes):
        if flag:
            print(prime)

if __name__ == "__main__":
    main()