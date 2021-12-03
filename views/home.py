import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template(template_file='home/index.html')
def index():
    return {
        'package_count': 274_000,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'packages': [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ]
    }


@router.get("/about")
@template(template_file='home/about.html')
def about():
    return {}
