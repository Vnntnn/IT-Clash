width = 80
year = 0
cols = 0
lead = 0
gap = 0

wdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
months = [
    {"name": "January",   "days": 31, "start_wday": 0, "at": 0},
    {"name": "February",  "days": 28, "start_wday": 0, "at": 0},
    {"name": "March",     "days": 31, "start_wday": 0, "at": 0},
    {"name": "April",     "days": 30, "start_wday": 0, "at": 0},
    {"name": "May",       "days": 31, "start_wday": 0, "at": 0},
    {"name": "June",      "days": 30, "start_wday": 0, "at": 0},
    {"name": "July",      "days": 31, "start_wday": 0, "at": 0},
    {"name": "August",    "days": 31, "start_wday": 0, "at": 0},
    {"name": "September", "days": 30, "start_wday": 0, "at": 0},
    {"name": "October",   "days": 31, "start_wday": 0, "at": 0},
    {"name": "November",  "days": 30, "start_wday": 0, "at": 0},
    {"name": "December",  "days": 31, "start_wday": 0, "at": 0},
]

def space(n):
    print(" " * n, end="")

def init_months():
    global cols, gap, lead, year

    # Leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months[1]["days"] = 29

    y = year - 1
    months[0]["start_wday"] = (y * 365 + y // 4 - y // 100 + y // 400 + 1) % 7

    for i in range(1, 12):
        prev = months[i - 1]
        months[i]["start_wday"] = (prev["start_wday"] + prev["days"]) % 7

    cols = (width + 2) // 22
    while 12 % cols != 0:
        cols -= 1

    if cols > 1:
        gap = (width - 20 * cols) // (cols - 1)
        if gap > 4:
            gap = 4
    else:
        gap = 0

    lead = (width - (20 + gap) * cols + gap + 1) // 2

def print_row(row):
    global cols, lead, gap
    from_idx = row * cols
    to_idx = from_idx + cols

    # Print month names
    space(lead)
    for c in range(from_idx, to_idx):
        name = months[c]["name"]
        i = 0
        while i < (20 - len(name)) // 2:
            print(" ", end="")
            i += 1
        print(name, end="")
        i = 0
        while i < (20 - len(name) - (20 - len(name)) // 2 + (0 if c == to_idx - 1 else gap)):
            print(" ", end="")
            i += 1
    print()

    # Print weekday headers
    space(lead)
    for c in range(from_idx, to_idx):
        i = 0
        while i < 7:
            print(wdays[i], end="")
            if i < 6:
                print(" ", end="")
            i += 1
        if c < to_idx - 1:
            space(gap)
        else:
            print()

    # Print dates
    done = False
    while not done:
        done = True
        space(lead)
        for c in range(from_idx, to_idx):
            m = months[c]
            i = 0
            if m["at"] == 0:
                space(3 * m["start_wday"])
                i = m["start_wday"]
            while i < 7 and m["at"] < m["days"]:
                m["at"] += 1
                if m["at"] < 10:
                    print(" ", end="")
                print(m["at"], end=" ")
                i += 1
                done = False
            while i < 7:
                print("   ", end="")
                i += 1
            if c < to_idx - 1:
                space(gap - 1)
            m["start_wday"] = 0
        print()
    print()

def print_year():
    title = str(year)
    space((width - len(title)) // 2)
    print(title + "\n")
    row = 0
    while row * cols < 12:
        print_row(row)
        row += 1

def main():
    global year, width

    y = input("Input a valid year: ")
    i = 0
    n = 0
    while i < len(y):
        ch = y[i]
        if ch >= '0' and ch <= '9':
            n = n * 10 + (ord(ch) - ord('0'))
        else:
            print("Invalid input.")
            return
        i += 1

    if n <= 0:
        print("Year must be positive.")
        return

    year = n
    init_months()
    print_year()

main()
