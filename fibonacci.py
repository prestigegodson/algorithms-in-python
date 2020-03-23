calculations = 0
store = dict()


# BigO(2^n) Horrible
def fib_recursion(n):
    global calculations, store
    calculations += 1

    if n < 2:
        return n

    if n in store:
        return store.get(n)

    store[n] = fib_recursion(n-1) + fib_recursion(n-2)
    return store[n]


def fib_recursion_old(n):
    if n < 2:
        return n

    return fib_recursion_old(n-1) + fib_recursion_old(n-2)


# BigO(n) fair
def fib_iterative(n):
    array = [0, 1]

    index = 2
    while index <= n:
        array.append(array[index-1] + array[index-2])
        index += 1

    return array[n]


print(fib_recursion(10))
print(calculations)
