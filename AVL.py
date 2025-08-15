# AVL Search Tree Implementation

# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.bf = 0
        self.left = None
        self.right = None

# calculation of balance factor
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def balance_factor(root):
    if root is None:
        return 0
    root.bf = height(root.left) - height(root.right)
    return root.bf

# rotations for balancing
def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    balance_factor(y)
    balance_factor(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    balance_factor(x)
    balance_factor(y)
    return y

def rotation(root):
    # LL case
    if root.bf > 1 and root.left.bf >= 0:
        return rotate_right(root)
    # LR case
    if root.bf > 1 and root.left.bf < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    # RR case
    if root.bf < -1 and root.right.bf <= 0:
        return rotate_left(root)
    # RL case
    if root.bf < -1 and root.right.bf > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

# insertion of a node
def insert(root, value):
    if root is None:
        return Node(value)

    if value <= root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)

    balance_factor(root)
    return rotation(root)

# deletion of a node
def deletion(root, value):
    if root is None:
        return None

    if value < root.data:
        root.left = deletion(root.left, value)
    elif value > root.data:
        root.right = deletion(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = root.left
        while temp.right is not None:
            temp = temp.right
        root.data = temp.data
        root.left = deletion(root.left, temp.data)

    balance_factor(root)
    return rotation(root)

# display
def display(root):
    if root is None:
        return
    display(root.left)
    print(f"({root.data},{root.bf})", end=" ")
    display(root.right)

# main
root = Node(7)
a = [3, 10, 2, 5, 9, 1,6]

for i in a:
    root = insert(root, int(i))

display(root)
print()

root = deletion(root, 5)
display(root)

