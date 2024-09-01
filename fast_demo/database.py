from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_demo.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():  # pragma: no cover
    with Session(engine) as session:
        yield session


""" 
#pragma: no cover, o coverage indentifica que essa função não conta na cobertura,
mas somente usa em casos que realmente o test não precisa ser coberto.
"""
