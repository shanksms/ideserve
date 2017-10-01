##code to be written
from binary_tree import BinaryTree

def pre_order_traversal(root):
    print(root.data, end=' ')
    #print(root.left, root.right)
    if root.left != None and root.right != None:
         pre_order_traversal(root.left)
         pre_order_traversal(root.right)

if __name__ == '__main__':
    '''
        3
     1     2
    '''

    node1 = BinaryTree(None, None, 1)
    node2 = BinaryTree(None, None, 2)
    root = BinaryTree(node1, node2, 3)
    #if node1.left == None:
    #    print('Is none')
    pre_order_traversal(root)
    print()
