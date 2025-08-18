#Implementation of a Multi-Way Search Tree

class Node:
    def __init__(self,value):
        self.data = value
        self.left,self.right = None,None

def m_way(value):
    # m = 3
    return [Node(value),None]

def insert(root,value):
    if root == None:
        return m_way(value)
    
    for i in range(len(root)):
        if root[i] == None:
            root[i] = Node(value)
            for i in range(len(root)):
                for j in range(i,len(root)):
                    if root[i].data > root[j].data:
                        root[i],root[j] = root[j],root[i]

            return root

    
    for j in range(len(root)):

        if value < root[j].data:
            if j == 0:
                root[j].left = insert(root[j].left,value)
            else:
                root[j-1].right = insert(root[j-1].right,value)
            return root
        
    for j in range(len(root)-1,-1,-1):

        if value > root[j].data:
            if j == len(root)-1:
                root[j].right = insert(root[j].right,value)
                return root

    return root

def display(root):
    if root == None:
        return None
    
    display(root[0].left)
    for i in range(len(root)):
        if root[i] == None:
            return None

        print(root[i].data,end = " ")
        display(root[i].right)

#main program
root = m_way(7)
l = [9,3,2,8,10,5,6]
for i in l:
    root = insert(root,i)

display(root)