

# Реализовать стек и очередь с помощью списка.
#
# Дополнительно реализовать другие рассмотренные на уроке структуры.

import random

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if self.items == []:
            return "Стек пуст."
        return "Стек не пуст."

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return "Очередь пуста."
        return "Очередь не пуста."

    def size(self):
        return len(self.items)

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.value, end=' ')
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.value, end=' ')
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.value, end=' ')


class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def printGraph(self):
        for i in self.graph:
            print(i, "->", " -> ".join(map(str, self.graph[i])))



print("Реализуем стек с помощью списка.")

stack = Stack()
print(stack.items)
print(stack.is_empty())
# if stack.is_empty():
#     print("Стек пуст.\n")
print("Заполняем стек:")

for st in range(10):
    stack.push(random.randint(1, 100))

print(stack.items)
print(f'Верхний элемент стека: {stack.peek()}')
print(f'Размер стека: {stack.size()}')
print(f'{stack.is_empty()}\n')

print("Реализуем очередь с помощью списка.")

queue = Queue()
print(queue.items)
print(queue.is_empty())
print("Заполняем очередь:")

for q in range(10):
    queue.enqueue(random.randint(1, 100))

print(queue.items)
print(f'Размер очереди: {queue.size()}')
print(f'Удаляем первый элемент из очереди: {queue.dequeue()}')
print(f'Размер очереди: {queue.size()}')
print(queue.is_empty())
print(f'Все элементы очереди: {queue.items}\n')


print("Реализуем дерево.")

root = Node(random.randint(1, 100))
print(f'Выбранный корень дерева: {root.value}')
print(f'Формируем дерево.')

for rt in range(10):
    root = insert(root, random.randint(1, 100))

print(f'Выводим дерево симметрично:')
print_inorder(root)
print("")
print(f'Выводим дерево прямо:')
print_preorder(root)
print("")
print(f'Выводим дерево обратно:')
print_postorder(root)
print("\n")

print("Реализуем граф.")

g = Graph()

for gs in range(20):
    g.addEdge(random.randint(1, 10), random.randint(1, 10))

g.printGraph()