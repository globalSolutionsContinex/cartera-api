import json
import uuid
from api.client import repository


class Client:
    def __init__(self, config):
        self.config = config
        self.repo = repository.Repo(self.config.POSGRES)
        self.client_attrs = ["id", "name", "payment"]
        client1 = {
                "id": 'wxctfvygbhnjmkl',
                "name": 'Vilariño',
                "subs_value": 300000,
                "period": {
                    "year": 2020,
                    "months": [
                        {"id": 1, "value": 300000, "isPay": True},
                        {"id": 2, "value": 300000, "isPay": False},
                        {"id": 3, "value": 300000, "isPay": False},
                        {"id": 4, "value": 300000, "isPay": False},
                        {"id": 5, "value": 300000, "isPay": False},
                        {"id": 6, "value": 300000, "isPay": False},
                        {"id": 7, "value": 300000, "isPay": False},
                        {"id": 8, "value": 300000, "isPay": False},
                        {"id": 9, "value": 300000, "isPay": False},
                        {"id": 10, "value": 300000, "isPay": False},
                        {"id": 11, "value": 300000, "isPay": False},
                        {"id": 12, "value": 300000, "isPay": False},
                    ]
                }
            }
        client2 = {
                "id": 'tfcvygbhunjimokjhg',
                "name": 'Ormeño',
                "subs_value": 300000,
                "periods": [
                        {"month": 1, "value": 300000, "isPay": True, "year": 2020},
                        {"id": 2, "value": 300000, "isPay": False},
                        {"id": 3, "value": 300000, "isPay": False},
                        {"id": 4, "value": 300000, "isPay": False},
                        {"id": 5, "value": 300000, "isPay": False},
                        {"id": 6, "value": 300000, "isPay": False},
                        {"id": 7, "value": 300000, "isPay": False},
                        {"id": 8, "value": 300000, "isPay": False},
                        {"id": 9, "value": 300000, "isPay": False},
                        {"id": 10, "value": 300000, "isPay": False},
                        {"id": 11, "value": 300000, "isPay": False},
                        {"id": 12, "value": 300000, "isPay": False},
                    ],
            }
        self.clients = [client1, client2]

    def get_list(self, year):
        return self.repo.get_clients_by_year(year)

    def create(self, request):
        client_f = json.loads(request.data)
        client_f["id"] = uuid.uuid4().hex
        periods = self.build_periods(client_f["periods"], client_f["id"])
        self.repo.upsert_period_values(periods)
        client = self.build_client(client_f)
        if client:
            self.repo.upsert_client(client)
        return client

    def update(self, request):
        client = json.loads(request.data)
        for cl in self.clients:
            if client["id"] == cl["id"]:
                cl["name"] = client["name"]
                cl["subs_value"] = client["subs_value"]
                cl["period"] = client["period"]
                for month in cl["period"]["months"]:
                    if not month["isPay"] and cl["subs_value"] != month["value"]:
                        month["value"] = cl["subs_value"]
                client = cl

        return client

    def build_client(self, client_f):
        client = {}
        for attr in self.client_attrs:
            client[attr] = client_f[attr]
        return client

    @staticmethod
    def build_periods(periods, client_id):
        for p in periods:
            p["client_id"] = client_id
        return periods
