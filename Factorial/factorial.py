'''Iterative'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

'''Recursion'''
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("Enter the value: "))
print("Iterative Factorial of", num, ":", factorial_iterative(num))
print("Recursive Factorial of", num, ":", factorial_recursive(num))
