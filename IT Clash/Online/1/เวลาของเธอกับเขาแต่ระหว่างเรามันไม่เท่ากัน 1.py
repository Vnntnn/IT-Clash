"""เวลาของเธอกับเขาแต่ระหว่างเรามันไม่เท่ากัน 1"""


def main():
    """Main fucntion"""
    n, m = input().split(" <-> ")
    n = int(n)
    m = int(m)
    V1 = int(input())
    V2 = int(input())

    day_somchai = n
    day_kochchasan = m

    found = False

    while day_somchai <= m and day_kochchasan >= n:
        if day_somchai == day_kochchasan:
            print(day_somchai)
            found = True
            day_somchai = m + 1
        else:
            day_somchai += V1
            day_kochchasan -= V2

    if not found:
        print("So sadly doe TT.")


main()
