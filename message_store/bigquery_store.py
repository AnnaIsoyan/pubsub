from google.cloud import bigquery

class BigQueryStore:
    def __init__(self, project_id, dataset_id, table_id):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id

        self._client = bigquery.Client(project=self.project_id)
        self._dataset = bigquery.DatasetReference(self.project_id, self.dataset_id)
        self._table = self._dataset.table(self.table_id)

    def create_data(self, data):
        errors = self._client.insert_rows_json(self._table, [data])
        if errors:
            raise Exception(f"Error inserting rows: {errors}")

