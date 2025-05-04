"""

เลขนี้พี่ขอ + 1

1 star

"""

def form(num: str):
    """
    Checking number formatting
    """
    comma = False
    watersym = False
    c_cnt = 0
    w_cnt = 0

    for i in range(len(num)):
        if c_cnt > 2:
            return "ERROR !"

        if i == len(num) - 1 and watersym and w_cnt != 3:
            return "ERROR !"

        if num[i] == ".":
            comma = True
        elif num[i] == ",":
            watersym = True
        elif num[i].isdigit():
            if watersym:
                w_cnt += 1
                if w_cnt > 3:
                    return "ERROR !"
            elif comma:
                c_cnt += 1
                if c_cnt > 2:
                    return "ERROR !"

    return int(num) + 1
    
def main():
    """Main function"""
    print(form(input()))

main()
