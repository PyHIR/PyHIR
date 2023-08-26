'''Routing module for the main API'''

import logging
from fastapi import APIRouter

from ..models.operationoutcome import make_operation_outcome
from ..util.settings import db_url
from ..util.database import init_database

# Create logger
logger = logging.getLogger('pyhir.routers.apirouter')

apirouter = APIRouter()


@apirouter.on_event('startup')
def connect_to_db_and_init():
    '''Connect to the DB and check if the schema is already populated, if not, initialize the tables'''
    try:
        init_database(db_conn_string=db_url)
    except ValueError as error:
        logger.error(f'There was an error initializing the database: {error}')
        raise error


@apirouter.get("/")
def root():
    '''Root return function for the API'''
    logger.info('Retrieved root of API')
    return make_operation_outcome('processing', 'This is the base URL of API. Unable to handle this request as it is the root.')
