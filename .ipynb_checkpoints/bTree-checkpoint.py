import sys
sys.path.append("Python")
from BSTree import main
def inorder(root):
    '''
    Objective: To perform in-order traversal of BST
    Input Parameter: root (Node) - root of the BST
    Return Value: None
    '''
    if root is not None:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)
def preorder(root):
    '''
    Objective: To perform pre-order traversal of BST
    Input Parameter: root (Node) - root of the BST
    Return Value: None
    '''
    if root is not None:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    '''
    Objective: To perform post-order traversal of BST
    Input Parameter: root (Node) - root of the BST
    Return Value: None
    '''
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')