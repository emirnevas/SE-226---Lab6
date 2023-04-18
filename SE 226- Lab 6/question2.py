result = 0

def sum_computer(n):

    global result
    if n <= 0:
        result = 0
    else:
        sum_computer(n - 1)
        result += (-1)**(n + 1) / n


n = int(input("Enter the value of n: "))
	
sum_computer(n)

print("Sum: %s" %result)
