class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # Если дерево пустое, возвращаем новый узел
    if root is None:
        return Node(key)
    else:
        # Иначе рекурсивно спускаемся по дереву
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(root, level=0, prefix="Корень: "):
    # Функция для наглядного текстового вывода иерархии
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            # L - левая ветвь, R - правая ветвь
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# Создание дерева и добавление узлов
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Вывод структуры
print("Иерархия бинарного дерева:")
print_tree(root)
