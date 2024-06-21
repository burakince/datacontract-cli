import os

import yaml


def to_trino_soda_configuration(server):
    # with service account key, using an external json file
    soda_configuration = {
        f"data_source {server.type}": {
            "type": "trino",
            "host": server.host,
            "port": str(server.port),
            "username": os.getenv("DATACONTRACT_TRINO_USERNAME"),
            "password": os.getenv("DATACONTRACT_TRINO_PASSWORD"),
            "catalog": server.catalog,
            "schema": server.schema_,
        }
    }

    soda_configuration_str = yaml.dump(soda_configuration)
    return soda_configuration_str
