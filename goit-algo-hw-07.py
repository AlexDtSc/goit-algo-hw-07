##### ДЗ. Тема 7. Дерева та балансування

### Завдання 1

'''
Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

Критерії прийняття:
Код виконується, і функція знаходить найбільше значення в дереві.
'''


# Двійкове дерево пошуку

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current



def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)



## Алгоритм (функція), який знаходить найбільше значення у двійковому дереві пошуку 

def max_value_root(root):
    current = root
    while current.right:
        current = current.right
    return current.val

max_value = max_value_root(root) 
print(f'Найбільше значення у двійковому дереві пошуку = {max_value}')



### Завдання 2

'''
Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

Критерії прийняття:
Код виконується, і функція знаходить найменше значення в дереві.
'''


# Двійкове дерево пошуку

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current



def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)


## Алгоритм (функція), який знаходить найменше значення у двійковому дереві пошуку 

def min_value_root(root):
    current = root
    while current.left:
        current = current.left
    return current.val

min_value = min_value_root(root) 
print(f'Найменше значення у двійковому дереві пошуку = {min_value}')




### Завдання 3

'''
Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

Критерії прийняття:
Код виконується, і функція знаходить суму всіх значень у дереві.
'''


# Двійкове дерево пошуку

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current



def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)


## Алгоритм (функція), який  знаходить суму всіх значень у двійковому дереві пошуку 


# Варіант 1. Із використанням глобальної змінної sum_value - краще не так не робити. 

# Чому? - 
# 1) Погана практика використовувати global. Це знижує читабельність і передбачуваність коду. 
# Якщо ти забудеш скинути sum_value = 0 перед новим викликом — отримаєш помилкову суму (накопичиться з попереднього запуску). Функція перестає бути чистою (pure function), бо має зовнішні залежності. 
# 2) Функція не повертає значення. Її не можна використати в інших обчисленнях, лише як процедуру, що щось змінює зовні.

# Варіант 1. Із використанням глобальної змінної sum_value - краще не так не робити. 
# Реалізація зворотного обходу дерева (ліве піддерево -> праве піддерево -> корінь) для суми всіх значень у двійковому дереві пошуку : (хоча можна теж саме робити і прямим обходом дерева і центровим обходом дерева просто змінюється порядок дій)

sum_value = 0
def postorder_traversal_sum(root):
    global sum_value
    if root:
        postorder_traversal_sum(root.left)
        postorder_traversal_sum(root.right)
        # print(root.val)                      # розкоментувати у випадку необхідності наочності виведення послідовно кожного вузла, сама функція суми всіх значень у двійковому дереві пошуку реалізації цього кроку не вимагає
        sum_value += root.val

# print("Зворотний обхід:")                    # розкоментувати у випадку необхідності наочності виведення послідовно кожного вузла, сама функція суми всіх значень у двійковому дереві пошуку реалізації цього кроку не вимагає
postorder_traversal_sum(root)

print(f'Сума всіх значень у двійковому дереві пошуку = {sum_value}')



# Варіант 2. Рекурсивне повернення суми - надійніший варіант
# Реалізація прямого обходу дерева (корінь -> ліве піддерево -> праве піддерево)  для суми всіх значень у двійковому дереві пошуку (): (хоча можна теж саме робити і центровим дерева і зворотним обходом дерева просто змінюється порядок дій)

def preorder_sum(root):
    if not root:
        return 0
    # print(root.val)  # розкоментувати у випадку необхідності наочності виведення послідовно кожного вузла, сама функція суми всіх значень у двійковому дереві пошуку реалізації цього кроку не вимагає
    return root.val + preorder_sum(root.left) + preorder_sum(root.right)

# print('Прямий обхід двійкового дерева пошуку') # розкоментувати у випадку необхідності наочності виведення послідовно кожного вузла, сама функція суми всіх значень у двійковому дереві пошуку реалізації цього кроку не вимагає
sum_value = preorder_sum(root)
print(f'Сума всіх значень у двійковому дереві пошуку = {sum_value}')



# # Візуалізація двійкового дерева пошуку

# from graphviz import Digraph

# def visualize_tree(node):
#     dot = Digraph()
#     def add_nodes_edges(node):
#         if not node:
#             return
#         dot.node(str(id(node)), str(node.val))
#         if node.left:
#             dot.node(str(id(node.left)), str(node.left.val))
#             dot.edge(str(id(node)), str(id(node.left)))
#             add_nodes_edges(node.left)
#         if node.right:
#             dot.node(str(id(node.right)), str(node.right.val))
#             dot.edge(str(id(node)), str(id(node.right)))
#             add_nodes_edges(node.right)
#     add_nodes_edges(node)
#     return dot

# # Приклад використання
# dot = visualize_tree(root)
# dot.render('bst_tree', format='png', cleanup=True)  # Зберігає у файл bst_tree.png
# dot.view()





#### Завдання 4 (необов'язкове завдання)

'''
Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, які, в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.



Також візьміть до уваги наступні вимоги:

Реалізуйте клас Comment, що представляє собою окремий коментар. Він має зберігати текст коментаря, автора та список відповідей.
Метод класу add_reply має додавати нову відповідь до коментаря.
Метод класу remove_reply має видаляти відповідь із коментаря. Це має змінювати текст коментаря на стандартне повідомлення (наприклад, "Цей коментар було видалено.") і встановлювати прапорець is_deleted в True.
Метод display має рекурсивно виводити коментар та всі його відповіді, використовуючи відступи для відображення ієрархічної структури.


Приклад очікуваного результату:

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()


Виведення:

Бодя: Яка чудова книга!
    Цей коментар було видалено.
        Сергій: Не книжка, а перевели купу паперу ні нащо...
    Марина: Що в ній чудового?
'''

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = 'Цей коментар було видалено.' 
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level

        if self.is_deleted:
            print(f'{indent}{self.text}')                   # якщо коментар видалено - вивести тільки текст 'Цей коментар було видалено.' без автора і самого тексту коментаря
        else:
            print(f'{indent}{self.author}: {self.text}')

        for reply in self.replies:
            reply.display(level + 1)
        

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()


'''
Виведення:

Бодя: Яка чудова книга!
    Цей коментар було видалено.
        Сергій: Не книжка, а перевели купу паперу ні нащо...
    Марина: Що в ній чудового?
    '''