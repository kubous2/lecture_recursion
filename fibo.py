def recursive_nth_fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)

def main():
    n = 5

    """fib = [recursive_nth_fibo(num) for num in range(1,n+1)]
    print(fib)"""

    fib = []
    for num in range (1,n+1):
        fib.append(recursive_nth_fibo(num))
    print(fib)

if __name__ == "__main__":
    main()
