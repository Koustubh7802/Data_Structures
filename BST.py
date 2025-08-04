#BST implementation using python

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#insertion of a node
def insert(root,data):
    temp = Node(data)

    if root==None:
        return temp
    
    elif data<=root.data:
        root.left = insert(root.left,data)

    elif data>root.data:
        root.right = insert(root.right,data)

    return root

#inorder traversal
def display(root):
    if root==None:
        return None
    
    display(root.left)
    print(root.data,end = " ")
    display(root.right)

#deletion of a node
def deletion(root,value):

    if root == None:
        return None
    
    if root.data<value:
        root.right = deletion(root.right,value)
    elif root.data>value:
        root.left = deletion(root.left,value)
    
    elif root.data == value:

        if root.left==None and root.right==None:
            root = None
            return root
        
        elif root.left!=None and root.right==None:
            root = root.left
        
        elif root.right!=None and root.left==None:
            root = root.right

        else:
            temp = root.left
            while temp.right!=None:
                temp = temp.right
            root.data = temp.data
            root.left = deletion(root.left,root.data)

    return root

#main

root = Node(int(input("Enter the root node --> ")))

ch = 1
while ch == 1:
    print("To enter more nodes, press 1\nTo exit press 0")
    ch = int(input("\nEnter your choice : "))

    if ch!=1:
        break
    root = insert(root,int(input("Enter the value of element --> ")))
    