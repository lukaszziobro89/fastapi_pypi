from pathlib import Path

import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles

from data import db_session
from views import home, account, packages

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure():
    configure_templates()
    configure_routes()
    configure_db()


def configure_db():
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def configure_templates():
    fastapi_chameleon.global_init('templates')


if __name__ == '__main__':
    main()
else:
    configure()
