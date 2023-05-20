def get_fib(n):
    fib_prev = [0, 1]
    [print(i) for i in fib_prev[:n]]
    for _ in range(2, n):
        fib = sum(fib_prev)
        print(fib)
        fib_prev[0], fib_prev[1] = fib_prev[1], fib

get_fib(int(input(">")))
