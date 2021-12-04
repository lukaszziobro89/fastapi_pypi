import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/")
@template(template_file='home/index.html')
def index(request: Request):
    vm = IndexViewModel(request=request)
    return vm.to_dict()


@router.get("/about")
@template(template_file='home/about.html')
def about(request: Request):
    vm = ViewModelBase(request)
    # TODO: use the vm
    return {}
