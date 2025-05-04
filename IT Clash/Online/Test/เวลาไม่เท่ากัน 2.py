import random

def generate_case():
    n = random.randint(1, 31)
    m = random.randint(n, 31)
    V1 = random.randint(1, 10)
    V2 = random.randint(1, 10)
    nS = random.randint(1, 100)
    nK = random.randint(1, 100)
    i = random.randint(1, 20)  # number of rounds
    j = random.randint(1, 20)   # age difference per round
    return f"{n} <-> {m}\n{V1}\n{V2}\n{nS} {nK}\n{i} {j}\n"

# Generate 30 diverse test cases
test_cases = [generate_case() for _ in range(30)]

for i in test_cases:
    print(i)
