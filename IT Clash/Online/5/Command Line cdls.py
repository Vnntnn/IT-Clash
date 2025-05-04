"""


Command line - CD/LS

My first 5⭐ fully complete

- Find relation about Tree and Linked list combination
- Manual sorting (Custom sort), Implement sorting logic (Ascending -> Decending) order
- Manual String slicing
- Algorithms Thinking -> Implements multiples data structure and more highly traversal with DFS or BFS


ใครชีวิตว่างลองทำข้อนี้ดูครับ XD



"""


def get_char(s, index):
    """Get character instead brackets :>"""
    i = 0
    it = iter(s)
    while True:
        try:
            c = next(it)
            if i == index:
                return c
            i += 1
        except StopIteration:
            return ""


def get_length(s):
    """Get string len"""
    count = 0
    for _ in s:
        count += 1
    return count


def slice_string(s, start, end=None):
    """Slicing string without list method :<"""
    result = ""
    i = 0
    it = iter(s)
    while True:
        try:
            c = next(it)
            if i >= start and (end is None or i < end):
                result += c
            i += 1
        except StopIteration:
            break
    return result


class FileNode:
    def __init__(self, name, is_directory):
        """Initializing file node"""
        self.name = name
        self.is_directory = is_directory
        self.children = None
        self.next = None

    def insert_child_sortt(self, child):
        """Insert all files and directory in file linked list with sorting"""
        if self.children is None:
            self.children = child
            return
        if self.should_come_before(child, self.children):
            child.next = self.children
            self.children = child
            return
        current = self.children
        while current.next is not None and not self.should_come_before(
            child, current.next
        ):
            current = current.next
        child.next = current.next
        current.next = child

    def should_come_before(self, node1, node2):
        """Align file nodes for sorting insert"""
        if node1.is_directory and not node2.is_directory:
            return True
        if not node1.is_directory and node2.is_directory:
            return False
        return self.compare_names(node1.name, node2.name) < 0

    def compare_names(self, name1, name2):
        """Compare name for sorting"""
        name1_dot = name1.find(".")
        name2_dot = name2.find(".")
        name1_base = slice_string(name1, 0, name1_dot) if name1_dot != -1 else name1
        name1_ext = slice_string(name1, name1_dot + 1) if name1_dot != -1 else ""
        name2_base = slice_string(name2, 0, name2_dot) if name2_dot != -1 else name2
        name2_ext = slice_string(name2, name2_dot + 1) if name2_dot != -1 else ""
        base_cmp = self.compare_strings(name1_base, name2_base)
        if base_cmp != 0:
            return base_cmp
        if name1_ext and name2_ext:
            return self.compare_strings(name1_ext, name2_ext)
        elif name1_ext:
            return 1
        elif name2_ext:
            return -1
        return 0

    def compare_strings(self, s1, s2):
        """Compare string for sorting"""
        len1 = get_length(s1)
        len2 = get_length(s2)
        min_len = len1 if len1 < len2 else len2
        i = 0
        while i < min_len:
            c1 = get_char(s1, i)
            c2 = get_char(s2, i)
            if c1.isdigit() and not c2.isdigit():
                return -1
            if not c1.isdigit() and c2.isdigit():
                return 1
            c1_lower = c1.lower()
            c2_lower = c2.lower()
            if c1_lower != c2_lower:
                return -1 if c1_lower < c2_lower else 1
            if c1 != c2:
                return -1 if c1 < c2 else 1
            i += 1
        return -1 if len1 < len2 else (1 if len1 > len2 else 0)


class DirectoryGraph:
    def __init__(self):
        """Initializing directory"""
        self.directories = None
        self.target = ""
        self.directory_list = None

    def add_directory(self, name, items_str):
        """Add item to dir"""
        node = FileNode(name, True)
        temp = ""
        char_iter = iter(items_str)
        try:
            while True:
                char = next(char_iter)
                if char == ",":
                    item = temp.strip()
                    if item:
                        is_dir = item.find(".") == -1
                        child = FileNode(item, is_dir)
                        node.insert_child_sortt(child)
                    temp = ""
                else:
                    temp += char
        except StopIteration:
            if temp.strip():
                is_dir = temp.find(".") == -1
                child = FileNode(temp.strip(), is_dir)
                node.insert_child_sortt(child)
        if self.directories is None:
            self.directories = node
        else:
            current = self.directories
            while current.next is not None:
                current = current.next
            current.next = node
        dir_node = FileNode(name, True)
        if self.directory_list is None:
            self.directory_list = dir_node
        else:
            current = self.directory_list
            while current.next is not None:
                current = current.next
            current.next = dir_node

    def set_target(self):
        """Set last input to target"""
        current = self.directory_list
        while current.next is not None:
            current = current.next
        self.target = current.name


class FileSystemTraversal:
    def __init__(self, graph):
        """Initializing directory traversal"""
        self.graph = graph
        self.cd_count = 0
        self.ls_count = 0
        self.path_head = None

    def traverse(self):
        """Traverse all directories"""
        current = self.graph.directories
        head = FileNode(current.name, True)
        path_tail = head
        self.path_head = head
        while current.name != self.graph.target:
            self.cd_count += 1
            self.ls_count += 1
            child = current.children
            found = False
            while child is not None:
                if child.is_directory:
                    dir_found = self.find_directory_by_name(child.name)
                    if dir_found is not None:
                        new_node = FileNode(child.name, True)
                        path_tail.next = new_node
                        path_tail = new_node
                        current = dir_found
                        found = True
                        break
                child = child.next
            if not found:
                break
        print(f"cd: {self.cd_count + 1}")
        print(f"ls: {self.ls_count + 1}\n\nPath Target:")
        self.show_path(self.path_head)
        self.show_directories_and_f(self.path_head)

    def show_path(self, head):
        """Show files path to target directory"""
        temp = head
        out = ""
        while temp is not None:
            out += temp.name
            if temp.next is not None:
                out += " > "
            temp = temp.next
        print("C:\\Users>", out)

    def show_directories_and_f(self, head):
        """Show dir and files"""
        temp = head
        while temp is not None:
            self.show_directory_contents(temp)
            temp = temp.next

    def show_directory_contents(self, directory):
        """Show dir all files and sub dir"""
        print("\n<< " + directory.name + " >>")
        actual_dir = self.find_directory_by_name(directory.name)
        if actual_dir is None or actual_dir.children is None:
            print("Noob linked list bruh")
        else:
            child = actual_dir.children
            index = 1
            while child is not None:
                print(str(index) + ". " + child.name)
                child = child.next
                index += 1

    def find_directory_by_name(self, name):
        """find dir algorithms"""
        current = self.graph.directories
        while current is not None:
            if current.name == name:
                return current
            current = current.next
        return None


def main():
    """Main function"""
    n = int(input())
    graph = DirectoryGraph()
    count = 0
    while count < n:
        line = input().strip()
        if ":" in line:
            sep = line.find(":")
            name = slice_string(line, 0, sep).strip()
            contents = slice_string(line, sep + 1).strip()
            graph.add_directory(name, contents)
            count += 1
    graph.set_target()
    traversal = FileSystemTraversal(graph)
    traversal.traverse()


main()
