"""เวลาของเธอกับเขาแต่ระหว่างเรามันไม่เท่ากัน 2"""


def is_prime(n: int) -> bool:
    """Prime number checking"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def tmrIwill(
    n: int, m: int, v1: int, v2: int, nSom: int, nKoc: int, meet: int, allround: int
) -> None:
    """Logic funtion"""

    output = []
    total_meet = 0
    f_day, l_day = None, None
    f_info = ()
    l_info = ()

    for r in range(1, meet + 1):
        head = f"{"=" * 18} (Round {r}) {"=" * 18}\n"
        did_meet = False

        # ทำเหมือน 2 Pointers
        startSom, startKoc = n, m

        # อายุในรอบๆนั้น
        ageSom, ageKoc = nSom + (r - 1) * allround, nKoc - (r - 1) * allround

        # หาจุดตัด
        while startSom <= m and startKoc >= n:
            if startSom == startKoc:
                did_meet = True
                total_meet += 1
                if f_day is None or startSom < f_day:
                    f_day = startSom
                    f_info = (ageSom, ageKoc, r)
                if l_day is None or r > l_info[2]:
                    l_day = startSom
                    l_info = (ageSom, ageKoc, r)
                break
            startSom += v1
            startKoc -= v2

        if did_meet:
            age_S_print = ageSom if 1 <= ageSom <= 100 else "-"
            age_K_print = ageKoc if 1 <= ageKoc <= 100 else "-"
            head += f"Day {startSom}: Somchai {age_S_print} years, Kochchasan {age_K_print} years\n"
            v1 = min(v1 + 2, m)
            v2 = min(v2 + 2, m)
        else:
            head += "See you next time.\n"
            v1 = max(1, v1 - 1)
            v2 = max(1, v2 - 1)

        if is_prime(r):
            if ageSom < 100:
                nSom += 1
            if ageKoc > 1:
                nKoc -= 1

        output.append(head)

    if not total_meet:
        print('We are not born for "LOVE".')
        return

    print('This is what we call "LOVE".\n')

    for ro in output:
        print(ro, end="")

    print(f"\nTotal meetings: {total_meet}")
    f_age_S_print = f_info[0] if 1 <= f_info[0] <= 100 else "-"
    f_age_K_print = f_info[1] if 1 <= f_info[1] <= 100 else "-"
    l_age_S_print = l_info[0] if 1 <= l_info[0] <= 100 else "-"
    l_age_K_print = l_info[1] if 1 <= l_info[1] <= 100 else "-"

    print(
        f"First day {f_day}: Somchai {f_age_S_print} years, Kochchasan {f_age_K_print} years (Rounds {f_info[2]})"
    )
    print(
        f"Last day {l_day}: Somchai {l_age_S_print} years, Kochchasan {l_age_K_print} years (Rounds {l_info[2]})"
    )
    return


def main():
    """Main function"""
    n, m = map(int, input().split(" <-> "))
    V1 = int(input())
    V2 = int(input())
    nS, nK = map(int, input().split())
    i, j = map(int, input().split())

    tmrIwill(n, m, V1, V2, nS, nK, i, j)


main()
