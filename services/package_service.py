from typing import List, Optional

from data.package import Package


def release_count() -> int:
    return 1234


def package_count() -> int:
    return 4452


def latest_releases(limit: int = 5) -> List:
    return [
                {'id': 'fastapi', 'summary': "A great web framework"},
                {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
                {'id': 'httpx', 'summary': "Requests for an async world"},
            ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    return None
