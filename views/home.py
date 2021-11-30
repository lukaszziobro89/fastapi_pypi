import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template(template_file='home/index.html')
def index(user: str = 'anonymous'):
    return {
        'user_name': user
    }


@router.get("/about")
def about():
    return {}
