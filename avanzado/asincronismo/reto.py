import asyncio
import random

files = [
            {'name' : 'archivo1.txt'},
            {'name' : 'archivo2.txt'},
            {'name' : 'archivo3.txt'}
        ]

async def download_file(data):
    for file in data:
        print("Descargando archivo..")
        await asyncio.sleep(random.randint(5,10))
        print(f"{file.get('name')} descargado con exito")

asyncio.run(download_file(files))