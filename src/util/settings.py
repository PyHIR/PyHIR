'''Settings file for importing environmental variables'''
import os

# ================= Creating necessary variables from Secrets ========================
log_level = os.environ.get('LOG_LEVEL', 'info')
docs_prepend_url = os.environ.get("DOCS_PREPEND_URL", "")
deploy_url = os.environ.get("DEPLOY_URL", 'http://localhost/')
