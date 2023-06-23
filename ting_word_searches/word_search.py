from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    curr = []
    resultado = []
    # iteração sobre cada elemento da fila
    for f in range(len(instance)):
        arquivo_pesquisado = instance.search(f)
        arquivo = arquivo_pesquisado["nome_do_arquivo"]
        linhas = arquivo_pesquisado["linhas_do_arquivo"]
        # itera sobre cada linha do arquivo
        for i, linha in enumerate(linhas):
            if word.lower() in linha.lower():
                curr.append({"linha": i + 1})

    if curr:
        resultado.append(
            {
                "palavra": word,
                "arquivo": arquivo,
                "ocorrencias": curr,
            }
        )

    return resultado


def search_by_word(word, instance: Queue):
    curr = []
    resultado = []
    # iteração sobre cada elemento da fila
    for f in range(len(instance)):
        arquivo_pesquisado = instance.search(f)
        arquivo = arquivo_pesquisado["nome_do_arquivo"]
        linhas = arquivo_pesquisado["linhas_do_arquivo"]
        # itera sobre cada linha do arquivo
        for i, texto in enumerate(linhas):
            if word.lower() in texto.lower():
                curr.append(
                    {
                        "linha": i + 1,
                        "conteudo": texto,
                    }
                )

    if curr:
        resultado.append(
            {
                "palavra": word,
                "arquivo": arquivo,
                "ocorrencias": curr,
            }
        )

    return resultado
