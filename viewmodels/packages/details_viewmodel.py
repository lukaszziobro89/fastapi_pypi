from starlette.requests import Request

from services import package_service
from viewmodels.shared.viewmodel import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = 'fastapi'
        self.package = package_service.get_package_by_id(package_name)

        if not self.package:
            return
