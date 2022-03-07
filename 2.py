#1 fatorial
def fac(n):
    if n < 1:
        raise ValueError("Number must be greater then 0")
    else:
        return fac(n-1) * n
    return 1

# 2 somatorio ate 0
def somatorio(n):
    if n < 1:
        raise ValueError("Number must be greater then 0")
    else:
        return somatorio(n-1) + n
    return 0

#3 fib
def fib(n):
    if n < 1:
        raise ValueError("Number must be greater then 0")
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

#4 somatorio dos numeros inteiros entre k e j
# k = 10; j = 5
def somKJ(k,j):
    if j >= k:
        raise ValueError("J must be smaller then K")
    if k == j + 1:
        return 0
    print("k: " + str(k-1))
    return somKJ(k-1,j) + k-1
    
# 5 palindromo
def isPal(s):
    if len(s) == 0:
        return True
    if s[0] == s[-1]:
        return isPal(s[1:-1])
    else:
        return False

# 6 converte para binario
def convBase2(n):
    if n < 0:
        raise ValueError("Number must be greater or equal then 0")
    # base 0 e 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    # recursivo
    return str(convBase2(n//2)) + str(n % 2)

# 7 
def somArray(ar):
    # base
    if not len(ar):
        return 0
    else:
        return ar[-1] + somArray(ar[:-1])

# 8 maior elemento
def findBiggest(ar):
    # erro
    if len(ar) == 0:
        raise Exception("The array can't be empty")
    # base
    if len(ar) == 1:
        return ar[0]
    if ar[0] > ar[-1]:
        return findBiggest(ar[:-1])
    else:
        return findBiggest(ar[1:])
    