'''Routing module for the main API'''

import logging
from fastapi import APIRouter

# Create logger
logger = logging.getLogger('pyhir.routers.apirouter')

apirouter = APIRouter()


@apirouter.get("/")
def root():
    '''Root return function for the API'''
    logger.info('Retrieved root of API')
    return {'note': "This is going to be an OperationOutcome later"}
    # return make_operation_outcome('processing', 'This is the base URL of API. Unable to handle this request as it is the root.')
