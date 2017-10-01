##code to be written
from binary_tree import BinaryTree

def pre_order_traversal(root):
    print(root.data, end=' ')

    if root.left != None and root.right != None:
         pre_order_traversal(root.left)
         pre_order_traversal(root.right)
def in_order_traversal(root):

    if root.left != None:
         in_order_traversal(root.left)
    print(root.data, end=' ')

    if root.right != None:
         in_order_traversal(root.right)
def post_order_traversal(root):
    if root.left != None:
         post_order_traversal(root.left)

    if root.right != None:
         post_order_traversal(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    root = BinaryTree(
    BinaryTree(BinaryTree(None, None, 4), BinaryTree(None, None, 5), 2),
    BinaryTree(None, None, 3), 1)
    #if node1.left == None:
    #    print('Is none')
    '''
            1
      2              3
 4        5
    '''
    pre_order_traversal(root)
    # 3 1 2
    print()
    # 1 3 2
    in_order_traversal(root)
    print()
    post_order_traversal(root)
    print()
