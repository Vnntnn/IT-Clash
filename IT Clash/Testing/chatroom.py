"""Chat room"""


def chatroom():
    """Chat Room event"""
    users = []
    sep_line = 0

    while sep_line != 2:
        event = input()
        if event == "---":
            sep_line += 1
            continue

        if event.endswith(" joins the room"):
            user = event[:-16]
            if user not in users:
                users.append(user)
        elif event.endswith(" leaves the room"):
            user = event[:-16]
            if user in users:
                users.remove(user)

    print_status(users)

    while sep_line != 3:
        event = input()
        if event == "---":
            sep_line += 1
            continue

        if event.endswith(" joins the room"):
            user = event[:-16]
            if user in users:
                print("Error")
                continue
            users.append(user)
        elif event.endswith(" leaves the room"):
            user = event[:-16]
            if user not in users:
                print("Error")
                continue
            users.remove(user)
        else:
            print("Error")
            continue

        print_status(users)

def print_status(users):
    """Print chat room status"""
    if not users:
        print("no one online")
    elif len(users) == 1:
        print(f"{users[0]} online")
    elif len(users) == 2:
        print(f"{users[0]} and {users[1]} online")
    else:
        print(f"{users[0]}, {users[1]}, and {len(users) - 2} more online")


def main():
    """Main Function"""
    chatroom()


main()
