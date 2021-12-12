import datetime
from typing import List, Optional

import sqlalchemy.orm

from data.package import Package
from data.release import Release
from data import db_session


def release_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Release).count()
    finally:
        session.close()


def package_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(Package).count()
    finally:
        session.close()


def latest_releases(limit: int = 5) -> List[Package]:
    session = db_session.create_session()

    try:
        releases = session.query(Release)\
            .options(
            sqlalchemy.orm.joinedload(Release.package)
        ).order_by(Release.created_date.desc())\
            .limit(limit)\
            .all()
    finally:
        session.close()
    return [r.package for r in releases]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        id=package_name,
        summary="Summary",
        description="Details/description",
        home_page="www.wp.pl",
        license="MIT",
        author_name="Mark Newman"
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release(major_ver=1, minor_ver=2, build_ver=0, created_date=datetime.datetime.now())
