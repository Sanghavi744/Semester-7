
memo = {}

def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 13
    steps = 0
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        steps += 1
    return c, steps+1

def fibonacci_recur(n):
    def fib(n):
        if n < 0:
            return -1, 1
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return n, 1
        fib1, steps1 = fib(n - 1)
        fib2, steps2 = fib(n - 2)
        result = fib1 + fib2, steps1 + steps2 + 1
        memo[n] = result  # Memoize the result
        return result

    return fib(n)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("Iterative:", fibonacci_iter(n)[0])
    print("Steps:", fibonacci_iter(n)[1])
    print("Recursive:", fibonacci_recur(n)[0])
    print("Steps:", fibonacci_recur(n)[1])





''' This code calculates the nth Fibonacci number using both iterative and 
recursive methods with memoization for optimization. fibonacci_iter iteratively 
computes the Fibonacci number and counts the steps required, while fibonacci_recur 
recursively calculates it with memoization to avoid redundant computations. The code 
defines a memo dictionary to store already computed values. It takes user input for n,
prints the result of both methods, and displays the number of steps taken in each 
case. The code demonstrates a comparison between the efficiency of the two approaches
for calculating Fibonacci numbers.'''


'''The Fibonacci sequence, also known as Fibonacci numbers, is defined as the sequence
of numbers in which each number in the sequence is equal to the sum of two numbers 
before it. '''

