import vehicle_listener.database as database
from vehicle_listener.utils import parse, validate
import aiohttp


BATCH_SIZE = 50


async def collect(socket):
    documents = list()

    while True:
        income = await socket.receive()

        if income.type == aiohttp.WSMsgType.TEXT:
            json_doc = parse(income.data)
            if validate(json_doc):
                documents.append(json_doc)
            if (len(documents) == BATCH_SIZE):
                await database.store(documents)
                documents = list()

        if income.type == aiohttp.WSMsgType.CLOSED:
            print('Socket is closed')
            return


async def process():
    async with aiohttp.ClientSession() as client:
        async with client.ws_connect('ws://127.0.0.1:8080') as socket:
            print('Connected to ws://127.0.0.1:8080')
            await collect(socket)
