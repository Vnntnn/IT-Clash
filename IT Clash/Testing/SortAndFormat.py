"""
Sort and format numbers from array

1 star

"""

def insertion_sort(arr: list) -> list:
    """Insertion sorting"""
    for i in range(len(arr)):
        walker = i
        for j in range(len(arr)):
            if arr[walker] < arr[j]:
                arr[j], arr[walker] = arr[walker], arr[j]

    return arr

def format_arr(arr: list) -> str:
    """Formatting numbers with commas and ranges"""
    f_arr = ""
    start = ""
    end = ""
    f_chk = False

    for i in range(len(arr)):
        f_num = f"({arr[i]})" if int(arr[i]) < 0 else str(arr[i])

        if i + 1 < len(arr) and int(arr[i]) + 1 == int(arr[i + 1]):
            if f_chk:
                end = f_num
            else:
                f_chk = True
                start = f_num
        else:
            if f_chk:
                end = f_num
                f_arr += f"{start}-{end},"
                start, end = "", ""
            else:
                f_arr += f"{f_num},"
            f_chk = False

    return f_arr.rstrip(",")

def main():
    """Main function"""
    import json

    s_arr = insertion_sort(json.loads(input()))

    print(format_arr(s_arr))

main()
