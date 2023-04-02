# PyHIR

An open-source, Python implementation of a FHIR server using the FastAPI framework, supported by SQLAlchemy for database transactions

## Database

This project will use a custom schema that will be initialized upon startup if the tables are not found. If the tables are found, no action will occur.

As a starting point, PostgreSQL will the initially supported database type due to leveraging the JSONB data type and JSON operations available in PostgreSQL.