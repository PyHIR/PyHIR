'''File for Base SQLAlchemy Class'''

import logging

from sqlalchemy.orm import DeclarativeBase

logger = logging.getLogger('pyhir.models.db_models.base')


class Base(DeclarativeBase):
    pass
