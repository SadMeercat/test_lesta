# Реализация 1: Циклический буфер на основе списка
class CircularBufferList:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер буфера должен быть больше 0")
        self.buffer = [None] * size
        self.size = size
        self.head = 0  # Указывает на начало очереди
        self.tail = 0  # Указывает на конец очереди
        self.count = 0  # Количество элементов в буфере

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Буфер полон")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Буфер пустой")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def __repr__(self):
        return f"CircularBufferList({self.buffer}, head={self.head}, tail={self.tail})"

# Реализация 2: Циклический буфер на основе collections.deque
from collections import deque

class CircularBufferDeque:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Размер буфера должен быть больше 0")
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        if len(self.buffer) == self.buffer.maxlen:
            raise OverflowError("Буфер полон")
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise IndexError("Буфер пустой")
        return self.buffer.popleft()

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def is_empty(self):
        return len(self.buffer) == 0

    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"
