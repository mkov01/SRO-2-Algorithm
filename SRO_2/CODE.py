class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def display_tree_advanced(node, prefix="", is_left=True, is_root=True):
    if node is not None:
        # Формируем текущую строку с использованием символов веток
        if is_root:
            print(f"Root: {node.val}")
        else:
            connector = "├── L: " if is_left else "└── R: "
            print(f"{prefix}{connector}{node.val}")
        
        # Вычисляем отступ для следующих уровней
        new_prefix = prefix + ("│   " if is_left and not is_root else "    ")
        
        # Рекурсивный вызов для потомков
        if node.left or node.right:
            if node.left:
                display_tree_advanced(node.left, new_prefix, True, False)
            else:
                print(f"{new_prefix}├── L: None")
                
            if node.right:
                display_tree_advanced(node.right, new_prefix, False, False)
            else:
                print(f"{new_prefix}└── R: None")

if __name__ == "__main__":
    root = Node(50)
    nodes = [30, 70, 20, 40, 60, 80]
    for n in nodes:
        insert(root, n)
    
    print("Визуализация бинарного дерева поиска:")
    print("=" * 45)
    display_tree_advanced(root)
    print("=" * 45)