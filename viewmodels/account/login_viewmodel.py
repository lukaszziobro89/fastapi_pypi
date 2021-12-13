import validators
from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.email = ''
        self.password = ''

    async def load(self):
        form = await self.request.form()
        self.email = form.get('email').lower().strip()
        self.password = form.get('password').strip()

        if not self.email or not self.email.strip():
            self.error = "Email is required"
        elif not validators.email(self.email):
            self.error = "Not a valid email"
        if not self.password or not self.password.strip():
            self.error = "Password is required"
