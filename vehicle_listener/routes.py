import aiohttp_jinja2
import vehicle_listener.database as database


PAGINATION_SIZE = 50


@aiohttp_jinja2.template('index.html')
async def index(request):
    return


@aiohttp_jinja2.template('vehicles.html')
async def vehicles(request):
    page_id = int(request.match_info['page_id'])
    offset = page_id * PAGINATION_SIZE

    docs = await database.get(offset=offset, limit=PAGINATION_SIZE)

    prev_page = page_id if page_id == 0 else page_id - 1
    next_page = page_id if not len(docs) else page_id + 1

    return {'vehicles': docs, 'prev_page': prev_page, 'next_page': next_page}


def setup(app):
    app.router.add_get('/', index)
    app.router.add_get('/vehicles/page/{page_id}', vehicles)
