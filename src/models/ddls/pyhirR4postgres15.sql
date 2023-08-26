CREATE TABLE resource (
    id INT PRIMARY KEY,
    version INT,
    create_time TIMESTAMP NOT NULL,
    resource JSONB NOT NULL
);

CREATE TABLE resource_history (
    id INT,
    version INT,
    create_time TIMESTAMP NOT NULL,
    resource JSONB NOT NULL,
    PRIMARY KEY (id, version)
)

CREATE TABLE sp_number (
    sp_name VARCHAR,
    resource_id INT,
    sp_value NUMERIC
);

CREATE TABLE sp_date (
    sp_name VARCHAR,
    resource_id INT
    sp_value TIMESTAMP
);

CREATE TABLE sp_string (
    sp_name VARCHAR,
    resource_id INT
    sp_value VARCHAR
);

CREATE TABLE sp_token (
    sp_name VARCHAR,
    resource_id INT
    sp_value_system VARCHAR,
    sp_value_value VARCHAR
);

CREATE TABLE sp_reference (
    sp_name VARCHAR,
    resource_id INT
    sp_reference_resource_type VARCHAR,
    sp_reference_resource_id INT
);

CREATE TABLE sp_composite (
    sp_name VARCHAR,
    resource_id INT
    sp_value VARCHAR
);

CREATE TABLE sp_quantity (
    sp_name VARCHAR,
    resource_id INT
    sp_value_system VARCHAR,
    sp_value_units VARCHAR,
    sp_value_value VARCHAR,
);

CREATE TABLE sp_uri (
    sp_name VARCHAR,
    resource_id INT
    sp_uri VARCHAR
);