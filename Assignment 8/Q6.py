# Function to generate Fibonacci series up to n terms

def fibonacci_series(n):
    a, b = 1, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter number of terms: "))
result = fibonacci_series(n)

print("Fibonacci series:")
for num in result:
    print(num, end=" ")