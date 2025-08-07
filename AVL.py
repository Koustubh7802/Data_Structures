#AVL Search Tree Implementation

#Node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.bf = 0
        self.left = None
        self.right = None

#calculation of balance factor
def height(node):
    if node == None:
        return 0
    return 1 + max(height(node.left),height(node.right))
def balance_factor(root):
    if root == None:
        return 0
    
    root.bf = height(root.left) - height(root.right)
    return root.bf
    
#rotations for balancing
def rotation(root,value):

    if root.bf in [-1,0,1]:
        return root
    
    if value <= root.data:
        if root.left.bf in [-1,0,1]:
            if value <= root.left.data:
                #LL Problem -> Single Right Rotation
                t1 = root
                t2 = root.left.right
                root = root.left
                t1.left = t2
                root.right = t1
                balance_factor(t1)
                balance_factor(root)
            else:
                #LR Problem -> Left Right Rotation
                t1 = root.left
                t2 = root.left.right.left
                root.left = root.left.right
                t1.right = t2
                root.left.left = t1
                balance_factor(t1)

                k1 = root
                k2 = root.left.right
                root = root.left
                k1.left = k2
                root.right = k1
                balance_factor(k1)
                balance_factor(root)
        else:
            root.left = rotation(root.left,value)

    else:
        if root.right.bf in [-1,0,1]:
            if value > root.right.data:
                #RR problem -> Single Left Rotation
                t1 = root
                t2 = root.right.left
                root = root.right
                t1.right = t2
                root.left = t1
                balance_factor(t1)
                balance_factor(root)
            else:
                #RL Problem -> Right Left Rotation
                t1 = root.right
                t2 = root.right.left.right
                root.right = root.right.left
                t1.left = t2
                root.right.right = t1
                balance_factor(t1)

                k1 = root
                k2 = root.right.left
                root = root.right
                k1.right = k2
                root.left = k1
                balance_factor(k1)
                balance_factor(root)

        else:
            root.right = rotation(root.right,value)
    
    return root

#insertion of a node
def insert(root,value):

    if root==None:
        return Node(value)
    
    elif value<=root.data:
        root.left = insert(root.left,value)
        #root.bf += 1

    elif value>root.data:
        root.right = insert(root.right,value)
        #root.bf -= 1

    root.bf = balance_factor(root)
    root = rotation(root,value)
    return root

#display
def display(root):
    if root==None:
        return None
    
    display(root.left)
    print(f"({root.data},{root.bf})",end = " ")
    display(root.right)

#main
root = Node(20)
a = [15,30,9,17,37,5,11,16,18,35,40,1,6,10,12,38,42,7,13]

for i in a:
    root = insert(root,int(i))


display(root)