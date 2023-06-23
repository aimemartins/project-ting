from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    assert len(priority_queue) == 0

    priority_queue.enqueue({"qtd_linhas": 9, "nome": "arquivo9.txt"})
    priority_queue.enqueue({"qtd_linhas": 4, "nome": "arquivo4.txt"})
    priority_queue.enqueue({"qtd_linhas": 2, "nome": "arquivo2.txt"})
    priority_queue.enqueue({"qtd_linhas": 5, "nome": "arquivo5.txt"})
    priority_queue.enqueue({"qtd_linhas": 7, "nome": "arquivo7.txt"})
    priority_queue.enqueue({"qtd_linhas": 11, "nome": "arquivo11.txt"})
    priority_queue.enqueue({"qtd_linhas": 3, "nome": "arquivo3.txt"})

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(7)

    assert len(priority_queue) == 7

    assert priority_queue.search(1) == {
        "qtd_linhas": 2,
        "nome": "arquivo2.txt",
    }
    assert priority_queue.search(2) == {
        "qtd_linhas": 3,
        "nome": "arquivo3.txt",
    }

    priority_queue.dequeue() == {"qtd_linhas": 4, "nome": "arquivo4.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 2, "nome": "arquivo2.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 3, "nome": "arquivo3.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 9, "nome": "arquivo9.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 5, "nome": "arquivo5.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 7, "nome": "arquivo7.txt"}
    priority_queue.dequeue() == {"qtd_linhas": 11, "nome": "arquivo11.txt"}

    assert len(priority_queue) == 0
