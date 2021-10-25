import aiohttp_jinja2
import jinja2
from aiohttp import web
import vehicle_listener.listener as listener
import vehicle_listener.routes as routes


async def start_listener(app):
    app['websocket_task'] = app.loop.create_task(listener.process())


def init_app():
    app = web.Application()

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('vehicle_listener', 'templates'))

    # add websocket client
    app.on_startup.append(start_listener)

    routes.setup(app)
    return app


def main():
    app = init_app()
    web.run_app(app, host='127.0.0.1', port=8081)


if __name__ == '__main__':
    main()
