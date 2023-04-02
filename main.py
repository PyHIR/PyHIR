'''Main application file'''

import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from src.models.customformatter import CustomFormatter
from src.models.operationoutcome import make_operation_outcome
from src.routers import apirouter
from src.util.settings import deploy_url, log_level

logger = logging.getLogger('pyhir')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

if log_level == "DEBUG":
    logger.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)

# ================= FastAPI variables ==================================
app_title = 'PyHIR'
app_version = '0.1.0'
app = FastAPI(title=app_title,
                   version=app_version,
                   include_in_schema=True,
                   docs_url=None,
                   redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= Routers inclusion from src directory ===============

app.include_router(apirouter.apirouter)

# ================= Invalid Request Exception Handling =================

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc) -> JSONResponse:
    '''Formats all invalidated requests to return as OperationOutcomes'''
    request = str(request)
    return JSONResponse(make_operation_outcome('invalid', str(exc)), status_code=400)

# ================== Custom OpenAPI ===========================

def custom_openapi():
    '''Defines the custom OpenAPI schema handling'''
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app_title,
        version=app_version,
        description=f"This is a custom Open API Schema for {app_title}",
        routes=app.routes,
    )
    openapi_schema["servers"] = [{"url": deploy_url}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
