import random

def generate_case():
    n = random.randint(1, 31)
    m = random.randint(n, 31)
    V1 = random.randint(1, 10)
    V2 = random.randint(1, 10)
    return f"{n} <-> {m}\n{V1}\n{V2}\n"

t_case = [generate_case() for _ in range(30)]

for i in range(len(t_case)):
    print(f"Testcase number: {i + 1}")
    print(t_case[i])