import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

from infrastructure import cookie_auth
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

    # Create account
    account = user_service.create_account(vm.name, vm.email, vm.password)

    # Login user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response


@router.get("/account/login")
@template(template_file="account/login.html")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post("/account/login")
@template(template_file="account/login.html")
async def login(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = "The account does not exists or the password is wrong"
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get("/account/logout")
def logout():
    # Logout user
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
