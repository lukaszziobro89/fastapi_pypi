from typing import List


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
