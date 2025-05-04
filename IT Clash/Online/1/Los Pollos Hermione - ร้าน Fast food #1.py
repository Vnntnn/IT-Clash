"""Los Pollos Hermione - ร้าน Fast food #1"""


class Bill:
    def __init__(self, pos, name, date, price):
        """Initializing a bill"""
        self.pos = pos
        self.name = name
        self.date = date
        self.price = price

    def show_bill(self):
        """Show bill info"""
        return f"Item {self.pos + 1}: {self.name} {self.date} {self.price}"


class Node:
    def __init__(self, data):
        """Initializing node"""
        self.data = data
        self.next = None


class billLinkedList:
    def __init__(self):
        """Initializing linked list"""
        self.count = 0
        self.head = None

    def insert_bill(self, name, date, price):
        """Insert new bill to linked list"""
        new_bill = Node(Bill(self.count, name, date, price))

        if self.head is None:
            self.head = new_bill
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_bill
        self.count += 1

    def traverse(self):
        """Traverse all bills"""
        if self.head is not None:
            current = self.head
            print("LPH: ", end="")
            while current:
                if current.next is not None:
                    print(current.data.show_bill(), end=" -> ")
                else:
                    print(f"{current.data.show_bill()}")
                current = current.next


def main():
    """Main function"""
    lph_bills = billLinkedList()

    for _ in range(int(input())):
        name, date, price = input().split()
        lph_bills.insert_bill(name, date, price)

    lph_bills.traverse()


main()
