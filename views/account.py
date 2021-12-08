import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

router = fastapi.APIRouter()


@router.get("/account")
@template(template_file="account/index.html")
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get("/account/register")
@template(template_file="account/register.html")
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post("/account/register")
@template(template_file="account/register.html")
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    print("TODO: REDIRECT")
    return vm.to_dict()


@router.get("/account/login")
@template(template_file="account/login.html")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
def logout():
    return {}
