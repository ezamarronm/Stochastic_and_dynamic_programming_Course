import sys
def recursive_fibonacci(n):
    if n == 0 or n == 1: 
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def memoization_fibonacci(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        answer = memoization_fibonacci(n - 1, memo) + memoization_fibonacci(n - 2, memo)
        memo[n] = answer
        return answer
if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    n = int(input('Choose a number: '))
    # answer = recursive_fibonacci(n)
    answer = memoization_fibonacci(n)
    print(answer)