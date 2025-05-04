import random

def generate_test():
    types = ["M-", "W-", "E-", "S-", "T-", "I-"]

    t = types[random.randint(0, len(types) - 1)]
    d = f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1900, 2026)}"
    p = round(random.uniform(10.00, 5000.00), 2)

    return f"{t} {d} {p}"

def gen_round():
    r = random.randint(1, 20)
    return r

test = []

for _ in range(20):
    gg = []
    rr = gen_round()
    gg.append(rr)
    for _ in range(rr):
        gg.append(generate_test())
    test.append(gg)

for i in range(len(test)):
    print(f"Testcase number {i + 1}")
    for it in test[i]:
        print(f"{it}")
    print("\n")