from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self._items.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def search(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self._items) == 0
