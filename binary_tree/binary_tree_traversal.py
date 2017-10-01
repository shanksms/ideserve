##code to be written
from binary_tree import BinaryTree

def pre_order_traversal(root):
    print(root.data, end=' ')

    if root.left != None and root.right != None:
         pre_order_traversal(root.left)
         pre_order_traversal(root.right)
def in_order_traversal(root):

    if root.left != None:
         pre_order_traversal(root.left)
    print(root.data, end=' ')

    if root.right != None:
         pre_order_traversal(root.right)
def post_order_traversal(root):
    if root.left != None:
         pre_order_traversal(root.left)

    if root.right != None:
         pre_order_traversal(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':


    node1 = BinaryTree(None, None, 1)
    node2 = BinaryTree(None, None, 2)
    root = BinaryTree(node1, node2, 3)
    #if node1.left == None:
    #    print('Is none')
    '''
        3
     1     2
    '''
    pre_order_traversal(root)
    # 3 1 2
    print()
    # 1 3 2
    in_order_traversal(root)
    print()
    post_order_traversal(root)
    print()
