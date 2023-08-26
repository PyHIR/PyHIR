'''File for all database interactions'''
import logging

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.engine.base import Engine
from sqlalchemy.exc import OperationalError

from ..models.db_models.base import Base

logger = logging.getLogger('pyhir.util.database')


def connect_to_db(db_conn_string: str, return_engine: bool = False) -> Engine | Connection | str:
    '''Create a connection and return either the connection or the engine'''
    engine: Engine = create_engine(db_conn_string)
    try:
        connection: Connection = engine.connect()
        if return_engine:
            return engine
        return connection
    except OperationalError as e:
        return str(e)


def init_database(db_conn_string: str):
    '''Try creating connection and checking if database tables exist. If they exist, do nothing, if not, create them.'''

    logger.info('Connecting to database...')
    conn: Connection | str = connect_to_db(db_conn_string=db_conn_string) # type: ignore
    logger.info('Connected to database!')

    if isinstance(conn, str):
        raise ValueError(conn)

    logger.info('Checking if tables exist, and if not, creating them...')
    Base.metadata.create_all(conn)
    logger.info('Finished creating tables if they dont exist.')
