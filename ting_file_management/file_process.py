from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name = path_file.split("/")[
        -1
    ]  # Obtém apenas o nome do arquivo a partir do caminho
    # Deve-se ignorar arquivos que já tenham sido processados anteriormente
    if any(file_name == item["nome_do_arquivo"] for item in instance._items):
        print(f"O arquivo {file_name} já foi processado anteriormente.")
        return
    # Deve-se ignorar arquivos que não sejam do tipo .txt
    lines = txt_importer(path_file)
    # Deve-se ignorar arquivos que estejam vazios
    if len(lines) > 0:
        # Deve-se adicionar o arquivo na fila
        data = {
            "nome_do_arquivo": file_name,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(data)
        print(data)
    else:
        print(f"O arquivo {file_name} está vazio.")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
