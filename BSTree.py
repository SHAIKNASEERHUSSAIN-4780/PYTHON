import sys
sys.path.append("Python")
from bNode import Node
def main():
    '''
    Objective: To build a binary search tree
    Input Parameterr: None
    Return Value: None
    '''
    bst = Node(15)
    bst.right = Node(23)
    bst.right.right = Node(30)
    bst.right.left = Node(20)
    bst.left = Node(10)
    bst.left.left = Node(6)
    return bst
if __name__ == "__main__":
    main()