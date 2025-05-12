import random

def random_testcast(n):
    """random number"""
    print(n)
    for i in range(n):
        if i == n - 1:
            print(0)
            return

        leng = random.randint(1, n)
        print(leng, end=" ")

        for _ in range(leng):
            print(random.randint(1, n), end= " ")
        print()

random_testcast(7)