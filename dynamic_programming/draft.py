def fib(n):
    def draft(a, b, counter):
        # print(counter)
        if counter == n:
            return b
        return draft(b, a + b, counter+1)

    return draft(0, 1, 1)


def fib3(n: int) -> int:
    if n <= 2:
        return 1

    previous, fib_number = 0, 1
    for _ in range(n - 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


def fib1(n):
    a = 0
    b = 1
    # temp_sum = 0
    for i in range(n-1):
        temp_sum = a + b
        a = b
        b = temp_sum

    return(temp_sum)
# def draft(a, b, counter):
#     print(counter)
#     if counter == 7:
#         return b
#     return draft(b, a + b, counter+1)

def cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

@cache
def fib2(n):
    if n <= 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)

if __name__ == '__main__':
    print(fib3(9))


