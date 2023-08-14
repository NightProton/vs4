def fibo(n):
    fibo_series = [0, 1]
    while len(fibo_series) < n:
        next_num = fibo_series[-1] + fibo_series[-2]
        fibo_series.append(next_num)
    return fibo_series

# Taking input from the user
num_terms = 15

# Generating and printing Fibonacci numbers
fibo_series = fibo(num_terms)
print("Fibonacci series:", fibo_series)
