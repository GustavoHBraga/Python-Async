import datetime
import asyncio


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    
    print(f'Aguarde a geração de {quantidade} dados...')
    for idx in range(1, quantidade + 1):

        item = idx * idx
        await dados.put(f"{item}, {datetime.datetime.now()}")
        await asyncio.sleep(0.01)

    print(f'{quantidade} dados gerados com sucesso...')

async def processar_dados(quantidade: int, dados: asyncio.Queue):
    
    print(f'Aguarde o processamento de {quantidade} dados...')
    processados = 0

    while processados < quantidade:

        await dados.get()
        await asyncio.sleep(0.01)
        processados += 1

    print(f'Foram processados {processados} itens')

def main():
    total = 100
    dados = asyncio.Queue()
    print(f'Computando {total * 2:.2f} dados.')

    el = asyncio.get_event_loop()

    tarefa1 = el.create_task(gerar_dados(total, dados))
    tarefa2 = el.create_task(gerar_dados(total, dados))
    tarefa3 = el.create_task(processar_dados(total * 2, dados))

    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3)
    el.run_until_complete(tarefas)


if __name__ == '__main__':
    main()
