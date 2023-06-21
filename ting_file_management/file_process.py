from ting_file_management.file_management import txt_importer
from ting_file_management.abstract_queue import AbstractQueue
import sys


def process(path_file, instance: AbstractQueue):
    # Deve-se ignorar arquivos que já tenham sido processados anteriormente
    if any(path_file == item["nome_do_arquivo"] for item in instance._items):
        print(
            f"O arquivo {path_file} já foi processado anteriormente.",
            file=sys.stderr,
        )
        return
    # Deve-se ignorar arquivos que não sejam do tipo .txt
    lines = txt_importer(path_file)
    # Deve-se ignorar arquivos que estejam vazios
    if len(lines) > 0:
        # Deve-se adicionar o arquivo na fila
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(data)
        print(data)


def remove(instance):
    try:
        info = instance.dequeue()
        print(f"Arquivo {info['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        info = instance.search(position)
        print(info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
