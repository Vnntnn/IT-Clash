import random
import string

def random_string(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def random_extension():
    extensions = ['.txt', '.jpg', '.png', '.pdf', '.cpp', '.py', '.html', '.css', '.js']
    return random.choice(extensions)

def generate_test_case(num_directories, max_items):
    dir_head = None
    dir_tail = None

    class DirNode:
        def __init__(self, name):
            self.name = name
            self.next = None

    count = 0
    while count < num_directories:
        new_node = DirNode(random_string())
        if dir_head is None:
            dir_head = new_node
            dir_tail = new_node
        else:
            dir_tail.next = new_node
            dir_tail = new_node
        count += 1

    print(num_directories)
    current = dir_head
    while current is not None:
        items_output = ""
        # ต้องมี directory ตัวถัดไปเสมอ
        if current.next is not None:
            items_output += current.next.name

        # สุ่มไฟล์และ directory อื่น ๆ
        inner_count = 0
        extra_count = random.randint(1, max_items)
        while inner_count < extra_count:
            name = random_string()
            if random.randint(0, 1) == 0:
                name += random_extension()
            else:
                # ให้มั่นใจว่าไม่ชนกับ dir.next
                if current.next is None or name != current.next.name:
                    name = name
                else:
                    continue
            items_output += ", " + name
            inner_count += 1

        print(f"{current.name}: {items_output.strip(', ')}")
        current = current.next

for i in range(1):
    print("Testcase number: ", 11)
    generate_test_case(random.randint(100, 100), random.randint(5, 20))
    print()