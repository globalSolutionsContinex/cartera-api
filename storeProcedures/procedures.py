# BASE PATHS
base_path_client = "storeProcedures/client/{procedure}"

# STP
upsert_periods = base_path_client.format(procedure="upsert_periods.sql")
upsert_client = base_path_client.format(procedure="upsert_client.sql")
