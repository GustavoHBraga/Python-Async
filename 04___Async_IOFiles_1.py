import asyncio
import aiofiles

async def exemplo_arq1():
    async with aiofiles.open('registros.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)

async def exemplo_arq2():
    linhas = []
    async with aiofiles.open('registros.txt') as arquivo:
        async for linha in arquivo:
            linhas.append(linha)

def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(exemplo_arq2())
    el.close()

if __name__ == '__main__':
    main()
