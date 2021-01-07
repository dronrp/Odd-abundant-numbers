import math

def numberDivisors(n):
    divisors = [1]
    i = 3
    while i <= math.sqrt(n):
        if n%i == 0:
            if n/i == i:
                divisors.append(i)
            else:
                divisors.extend([i,n//i])
        i+=2
    return sum(divisors)

def oddAbundantNumbers():
    ans = []
    for i in range(9, 100000, 2):
        if i < numberDivisors(i):
            ans.append(i)
    print(ans)

if __name__ == "__main__":
    oddAbundantNumbers()
