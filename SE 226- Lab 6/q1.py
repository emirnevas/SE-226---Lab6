n = float(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)

power = lambda a, b: a ** b

e_n = lambda n, x: sum([power(n, i) / factorial(i) for i in range(x + 1)])

result = e_n(n, x)
print(f"e^{n} approximation with x terms: {result}")
