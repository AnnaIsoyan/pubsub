import os
from dotenv import load_dotenv
from subscriber import Subscriber
from message_store import MongoStore, BigQueryStore

load_dotenv()
project_id = os.getenv("PROJECT_ID")
dataset_id = os.getenv("DATASET_ID")
table_id = os.getenv("TABLE_ID")
db_name = os.getenv("MONGO_DBNAME")
collection_name = os.getenv("MONGO_COLLECTION")
google_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
subscription_id = os.getenv("SUBSCRIPTION_ID")


_mongo_store = MongoStore(db_name, collection_name)
#_bigquery_store = BigQueryStore(project_id, dataset_id, table_id)
_subscriber = Subscriber(project_id, subscription_id, google_credentials)
#_subscriber.set_bigquery_store(_bigquery_store)
_subscriber.set_mongo_store(_mongo_store)

if __name__ == "__main__":
    _subscriber.listen_store_messages()