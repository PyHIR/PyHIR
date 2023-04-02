'''File for all operations around OperationOutcomes'''

import logging

from fhir.resources.operationoutcome import OperationOutcome

logger = logging.getLogger('pyhir.models.operationoutcome')


def make_operation_outcome(code: str, diagnostics: str, severity: str = 'error'):
    '''
    Returns an OperationOutcome for a given code, diagnostics string, and a severity
    (Default of error)
    '''
    oo_template = {
        'issue': [
            {
                'severity': severity,
                'code': code,
                'diagnostics': diagnostics,
            }
        ]
    }
    return OperationOutcome(**oo_template).dict() # type: ignore