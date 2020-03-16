from infrastructure import postgres
from storeProcedures import procedures
import infrastructure.log as log
import json

class Repo:
    def __init__(self, connection):
        self.logger = log.get_logger("Client Repository")
        self.instance = postgres.Connector(connection)

    def get_clients_by_year(self, year):
        pass

    def upsert_client(self, client):
        try:
            return self.instance.execute_multiple_queries_select_dict_response(
                procedures.upsert_client, {"data": json.dumps([client])})

        except Exception as ex:
            self.logger.error(ex)
            raise ValueError(f'Error upserting client {client}')

    def upsert_period_values(self, periods):
        try:
            if len(periods) > 0:
                return self.instance.execute_multiple_queries_select_dict_response(
                    procedures.upsert_periods, {"data": periods})
        except Exception as ex:
            self.logger.error(ex)

