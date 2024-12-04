def is_prime(func):
    def wrapped(*args):
        c = 0
        total = func(*args)
        for i in range (1, 10):
            if total % i == 0:
                c += 1
        if c == 1:
            print("Простое")
        else:
            print("Составное")
        return total
    return wrapped


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total


result = sum_three(2, 3, 6)
print(result)