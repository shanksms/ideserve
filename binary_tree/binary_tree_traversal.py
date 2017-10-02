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
def level_order_traversal(root):
    level_elements_dict = {}
    level_order_traversal_helper(root, 0, level_elements_dict)
    for key, value in level_elements_dict.items():
        ls_of_str = [str(i) for i in value]
        print(" ".join(ls_of_str), end=' ')
def level_order_traversal_helper(root, level, level_elements_dict):
    if level in level_elements_dict:
        level_elements_dict[level].append(root.data)
    else:
        element_list = []
        element_list.append(root.data)
        level_elements_dict[level] = element_list
    if root.left != None:
        level_order_traversal_helper(root.left, level + 1, level_elements_dict)
    if root.right != None:
        level_order_traversal_helper(root.right, level + 1, level_elements_dict)





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
    #pre_order_traversal(root)
    #print()
    #in_order_traversal(root)
    #print()
    #post_order_traversal(root)
    #print()
    level_order_traversal(root)
    print()
