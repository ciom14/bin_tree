import unittest

#Рекурсивное построение бинарного дерева:
def gen_bin_tree(height, root):
    if height == 0:
        return None

    #Вычисляем потомков по формуле:
    left_leaf = root + root / 2
    right_leaf = root ** 2

    #Рекурсивно строим поддеревья:
    left_subtree = gen_bin_tree(height - 1, left_leaf)
    right_subtree = gen_bin_tree(height - 1, right_leaf)

    #Формируем узел дерева в виде словаря:
    node = {
        'root': root,
        'left': left_subtree,
        'right': right_subtree
    }

    return node

#Реализация с использованием списков:

def gen_bin_tree_list(height, root):
    if height == 0:
        return None
    left_leaf = root + root / 2
    right_leaf = root ** 2
    left_subtree = gen_bin_tree_list(height - 1, left_leaf)
    right_subtree = gen_bin_tree_list(height - 1, right_leaf)

    #Формируем узел дерева в виде списка:

    return [root, left_subtree, right_subtree]

class TestBinTree(unittest.TestCase):

    #Тесты для высоты 0:

    def test_gen_bin_tree_height_zero(self):
        self.assertIsNone(gen_bin_tree(0, 5))
    def test_gen_bin_tree_list_height_zero(self):
        self.assertIsNone(gen_bin_tree_list(0, 5))

    #Тесты для высоты 1:

    def test_gen_bin_tree_height_one(self):
        result = gen_bin_tree(1, 8)
        expected = {
            'root': 8,
            'left': None,
            'right': None
        }
        self.assertEqual(result, expected)
    def test_gen_bin_tree_list_height_one(self):
        result = gen_bin_tree_list(1, 8)
        expected = [8, None, None]
        self.assertEqual(result, expected)

    #Тесты на правильность работы:

    def test_gen_bin_tree(self):
        result = gen_bin_tree(2, 8)
        expected = {
            'root': 8,
            'left': {
                'root': 12.0,
                'left': None,
                'right': None
            },
            'right': {
                'root': 64,
                'left': None,
                'right': None
            }
        }
        self.assertEqual(result, expected)
    def test_gen_bin_tree_list(self):
        result = gen_bin_tree_list(2, 8)
        self.assertEqual(result[0], 8)
        self.assertEqual(result[1][0], 12.0)
        self.assertEqual(result[2][0], 64)
if __name__ == '__main__':
        unittest.main()



height = int(input("Введите высоту дерева: "))
root = int(input("Введите корень дерева: "))
choice = input("Вывод через словарь или список?: ")
if choice == "словарь":
    print("=== Бинарное дерево словарь ===")
    print(gen_bin_tree(height, root))
else:
    print("=== Бинарное дерево список ===")
    print(gen_bin_tree_list(height, root))

