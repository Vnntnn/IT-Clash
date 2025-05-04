"""Los Pollos Hermione - ร้าน Fast food #2"""


class Bill:
    def __init__(self, pos: int, type_: str, name: str, date: str, price: str):
        """Initializing bill"""
        self.pos = pos
        self.type = type_
        self.name = name
        self.date = date
        self.price = float(price)
        self.day, self.month, self.year = map(int, date.split("/"))

    def show(self, idx: int, typename: str):
        """Show bill info"""
        return f"Item {idx}: {typename}: {self.name} {self.date} {self.price}"


class Node:
    def __init__(self, data: Bill):
        """Initializing node"""
        self.data = data
        self.next = None


class billLinkedList:
    def __init__(self):
        """Initializing linked list"""
        self.count = 0
        self.head = None

    def insert(self, type_: str, name: str, date: str, price: str):
        """Insert sorted node to linked list"""
        new_bill = Node(Bill(self.count, type_, name, date, price))
        self.head = sorted_insert(self.head, new_bill)
        self.count += 1


def compare_all(b1: Bill, b2: Bill) -> int:
    """Compare date → price → name"""
    if b1.year != b2.year:
        return b1.year - b2.year
    if b1.month != b2.month:
        return b1.month - b2.month
    if b1.day != b2.day:
        return b1.day - b2.day

    if b1.price != b2.price:
        return -1 if b1.price > b2.price else 1

    return (b1.name > b2.name) - (b1.name < b2.name)


def sorted_insert(head: Bill, new_node: Bill) -> Bill:
    """Sorting bill to insert to linked list"""
    if head is None or compare_all(new_node.data, head.data) < 0:
        new_node.next = head
        return new_node

    current = head
    while (
        current.next is not None and compare_all(new_node.data, current.next.data) >= 0
    ):
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head


def sort_linked_listt(head: Bill) -> Bill:
    """Sort bill linked list"""
    result = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = None
        result = sorted_insert(result, current)
        current = next_node
    return result


def process_type(code: str, typename: str, head: Bill):
    """Showing type of bills"""
    total = 0
    count = 0
    result_head = None
    current = head
    while current is not None:
        if current.data.type == code:
            total += current.data.price
            count += 1
            new_node = Node(current.data)
            new_node.next = result_head
            result_head = new_node
        current = current.next

    result_head = sort_linked_listt(result_head)

    if count > 0:
        print(f"<< {typename} >>")
        idx = 1
        current = result_head
        while current is not None:
            print(current.data.show(idx, typename))
            idx += 1
            current = current.next
        print("Result:")
        print(f"Items Amount: {count} bills")
        print(f"Total Amount: {total:.2f} bath")
        print()
    return count, total


def main():
    """Main function"""
    lph_bills = billLinkedList()
    n = int(input())

    for _ in range(n):
        line = input()
        name_part, date, price = line.rsplit(" ", 2)
        bill_type, bill_name = name_part.split(": ", 1)

        for i in bill_type:
            bill_type = i
            break

        lph_bills.insert(bill_type, bill_name, date, price)

    print("Los Pollos Hermione -- List\n")
    total_bills = 0
    total_amount = 0

    io_count = 0

    typename_map = {
        "M": "Material",
        "W": "Water",
        "E": "Electricity",
        "S": "Salary",
        "T": "Tax",
    }

    for code in ("M", "W", "E", "S", "T"):
        typename = f"{code}-{typename_map.get(code)}"
        count, amt = process_type(code, typename, lph_bills.head)
        total_bills += count
        total_amount += amt

    for code in ("I", "O"):
        count, amt = process_type(code, "I/O-Income/Outcome", lph_bills.head)
        io_count += count
        total_amount += amt

    total_bills += io_count

    print("=== LPH Result: Los Pollos Hermione ===")
    print(f"LPH Items Amount: {total_bills} bills")
    print(f"LPH Total Amount: {total_amount:.2f} bath")
    if total_amount < 0:
        print("Mr.G is not happy.")
    elif total_amount == 0:
        print("Mr.G wanna go to bed rn.")
    else:
        print("Mr.G is happy.")


main()
