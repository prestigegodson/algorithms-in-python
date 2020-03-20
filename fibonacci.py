#BigO(n^2) Horrible
def fib_recursion(n):
    if n < 2:
        return n

    return fib_recursion(n-1) + fib_recursion(n-2)


#BigO(n) fair
def fib_iterative(n):
    array = [0, 1]

    index = 2
    while index <= n:
        array.append(array[index-1] + array[index-2])
        index += 1

    return array[n]
