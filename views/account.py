import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

from services import user_service
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

    account = user_service.create_account(vm.name, vm.email, vm.password)

    return fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)


@router.get("/account/login")
@template(template_file="account/login.html")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
def logout():
    return {}
