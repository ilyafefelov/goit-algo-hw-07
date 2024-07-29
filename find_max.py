# TreeNode: Клас для вузла дерева.
# get_height: Повертає висоту вузла.
# update_height: Оновлює висоту вузла.
# get_balance: Повертає баланс вузла.
# rotate_right: Виконує праве обертання.
# rotate_left: Виконує ліве обертання.
# insert: Вставляє новий ключ у дерево та балансує його.
# print_tree: Виводить дерево у зручному форматі.
# find_max_value: Знаходить найбільше значення у дереві.
# find_min_value: Знаходить найменше значення у дереві.
# sum_of_values: Знаходить суму всіх значень у дереві.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    if not node:
        return
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    if not node:
        return TreeNode(key)
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    update_height(node)

    balance = get_balance(node)

    # Left Left Case
    if balance > 1 and key < node.left.value:
        return rotate_right(node)

    # Right Right Case
    if balance < -1 and key > node.right.value:
        return rotate_left(node)

    # Left Right Case
    if balance > 1 and key > node.left.value:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # Right Left Case
    if balance < -1 and key < node.right.value:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def find_max_value(node):
    if node is None:
        return float('-inf')
    while node.right is not None:
        node = node.right
    return node.value

def find_min_value(node):
    if node is None:
        return float('inf')
    while node.left is not None:
        node = node.left
    return node.value

def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
root = None
values = [10, 5, 20, 2, 7, 15, 30, 25, 35, 40, 1, 6, 8, 9, 12, 18, 16, 17, 3, 4]

for value in values:
    root = insert(root, value)

print("Дерево:")
print_tree(root)
print("Максимальне значення у дереві:", find_max_value(root))
print("Мінімальне значення у дереві:", find_min_value(root))
print("Сума всіх значень у дереві:", sum_of_values(root))
