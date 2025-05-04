"""
Singly LinkedList,
Hashtable,
Sorting,
OOP
"""


class Employee:
    def __init__(self, name: str, emp_id: int, money: float):
        """Initializing emp"""
        self.name = name
        self.emp_id = emp_id
        self.money = money

    def show_info(self):
        """Show employee info"""
        print(f"Name : {self.name}\nID : {self.emp_id}\nMoney : {self.money:.2f}")
        print("---------------")


class Node:
    def __init__(self, data: Employee):
        """Initializing node"""
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """Iintializing SinglyLL"""
        self.head = None

    def insert(self, name: str, emp_id: int, money: float):
        """Insert
        1. check ID
        2. chek money
            if money == current money
                check id instead
        3. insert node
        4. done!!!
        """
        emp_id = self.rehash_id(emp_id)
        new_node = Node(Employee(name, emp_id, money))

        if (
            self.head is None
            or (money < self.head.data.money)
            or (money == self.head.data.money and emp_id < self.head.data.emp_id)
        ):
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and (
            current.next.data.money < money
            or (current.next.data.money == money and current.next.data.emp_id < emp_id)
        ):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def rehash_id(self, emp_id: int) -> int:
        """Rehash ID"""
        current = self.head
        while current is not None:
            if current.data.emp_id == emp_id:
                emp_id += 1
                current = self.head
            else:
                current = current.next
        return emp_id

    def traverse(self):
        """Traverse all nodes"""
        if self.head is None:
            print("LinkedLink is Empty.")
            return
        current = self.head
        while current is not None:
            current.data.show_info()
            current = current.next


def main():
    """Main function"""
    link = LinkedList()

    while (employee_input := input().strip()) not in ("END", "End", "end"):
        emp_splits = employee_input.split()
        name, emp_id, money = "", 0, 0.0

        i = 0
        for emp_inf in emp_splits:
            if i == 0:
                name = emp_inf
                i += 1
            elif i == 1:
                emp_id = int(emp_inf)
                i += 1
            elif i == 2:
                money = float(emp_inf)

        if money < 0:
            continue

        link.insert(name, emp_id, money)

    link.traverse()


main()
