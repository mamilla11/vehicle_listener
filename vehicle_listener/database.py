import time

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_USER = 'anonymous'
MONGO_PASS = 'JgOgGb3nmuPBM6qQ'
MONGO_CLUSTER = 'cluster0.qisre.mongodb.net'
MONGO_DB = 'vehiclesdb'
MONGO_QUERY_STR = 'retryWrites=true&w=majority'

MONGO_URI = 'mongodb+srv://{}:{}@{}/{}?{}'.format(
    MONGO_USER, MONGO_PASS, MONGO_CLUSTER, MONGO_DB, MONGO_QUERY_STR
)

MONGO_CONNECTION_ARGS = {
    'ssl': True,
    'ssl_cert_reqs': 'CERT_NONE',
    'zlibCompressionLevel': 7,
    'compressors': 'zlib'
}

db = AsyncIOMotorClient(MONGO_URI, **MONGO_CONNECTION_ARGS).vehiclesdb
db.vehicles.drop()


async def store(documents):
    start_time = time.time()
    await db.vehicles.insert_many(documents)
    print('Batch of {} documents was stored to database in {:.2f} s'.format(
        len(documents), time.time() - start_time
    ))


async def get(*, offset=0, limit=None):
    vehicles_cursor = db.vehicles.find().sort('_id').skip(offset)
    return await vehicles_cursor.to_list(limit)
