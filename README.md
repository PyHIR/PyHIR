# PyHIR

An open-source, Python implementation of a FHIR server using the FastAPI framework, supported by SQLAlchemy for database transactions

## Database

This project will use the HAPI FHIR database schema, and will populate the database using a DDL the first time an application starts up if the tables are not found. If the tables are already found, no schema operations will occur.

As a starting point, PostgreSQL will the initially supported database type.