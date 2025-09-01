#write a program to print a fibonnaci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
    return

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    fibonacci(n)


def square(n):
    print(f"The square of {n} is {n*n}")
