class Node:
    def __init__(self, city, count=1):
        self.city = city
        self.count = count
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(None, 0)  # Sentinel node, color is black
        self.TNULL.color = 'black'
        self.root = self.TNULL
        self.avg = 0;
        self.total = 0;
        self.total_cities = 0;

    def insert(self, city):
        new_node = Node(city)
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.parent = None
        self.total += 1;

        current = self.root
        parent = None

        while current != self.TNULL:
            parent = current
            if city == current.city:
                current.count += 1
                return
            elif city < current.city:
                current = current.left
            else:
                current = current.right
        self.total_cities += 1;
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.city < parent.city:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'black'
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle node
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle node

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def get_root(self):
        return self.root

    def in_order_traversal(self, node, result):
        if node != self.TNULL:
            self.in_order_traversal(node.left, result)
            result.append((node.city, node.count))
            self.in_order_traversal(node.right, result)

    def print_tree(self):
        result = []
        self.in_order_traversal(self.root, result)
        for city, count in result:
            print(f'{city}: {count}')

    def get_height(self, node):
        if node == self.TNULL:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)

    def get_tree_height(self):
        return self.get_height(self.root)
    
    def search(self, city):
        current = self.root
        city = city.lower()
        while current != self.TNULL:
            if current.city.lower() == city:
                return current.count
            elif city < current.city.lower():
                current = current.left
            else:
                current = current.right
        return self.avg;

    def set_avg(self):
        self.avg = self.total/self.total_cities



def main():
    cities = ["New York", "Los Angeles", "Chicago", "New York", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Detroit", "Nashville", "Portland", "Memphis", "Oklahoma City", "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Omaha", "Colorado Springs", "Raleigh", "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Tampa", "Arlington"]

    # Initialize Red-Black Tree
    tree = RedBlackTree()

# Insert cities into the Red-Black Tree
    for city in cities:
        tree.insert(city)
    tree.set_avg()
    
    print(tree.total)
    print(tree.total_cities)
# Print the tree
    tree.print_tree()
    print(tree.get_tree_height())
    print(len(cities))

    print(tree.search("New York"))

main()