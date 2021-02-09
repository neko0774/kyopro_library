def is_prime(number):
    i = 2
    while i*i <= number:
        if number%i==0:
            return 1
        i+=1
    return 0


def factorization(x):
    i = 2
    ans = []
    while i**2 <= x:
        e = 0
        while x%i == 0:
            e += 1
            x //= i
        if e>0:
            ans.append([i, e])
        i += 1
    if x!=1: ans.append([x, 1])
    return ans