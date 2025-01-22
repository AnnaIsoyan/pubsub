import json
from google.cloud import pubsub_v1
from message_store import MongoStore, BigQueryStore


class Subscriber:
    def __init__(self, project_id: str, subscription_id: str, google_credentials: str):
        self.project_id = project_id
        self.subscription_id = subscription_id
        self.google_credentials = google_credentials
        self._mongo_store = None
        self._bigquery_store = None

        if not all([self.project_id, self.subscription_id, self.google_credentials]):
            raise ValueError(
                "Environment variables for project_id, subscription_id, and google_credentials must be set.")

        # Pub/Sub subscriber
        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(self.project_id, self.subscription_id)

    def set_mongo_store(self, mongo_store: MongoStore):
        self._mongo_store = mongo_store

    def set_bigquery_store(self, bigquery_store: BigQueryStore):
        self._bigquery_store = bigquery_store

    def callback(self, message):
        try:
            # Parse the message data as JSON
            _data = json.loads(message.data.decode("utf-8"))

            if self._bigquery_store is not None:
                # Insert into BigQuery
                self._bigquery_store.create_data(_data)

            if self._mongo_store is not None:
                # Insert into MongoDB
                self._mongo_store.insert_data(_data)

            message.ack()

        except Exception as e:
            print(f"Error processing message: {e}")
            message.nack()

    def listen_store_messages(self):
        print("Listening for messages on Pub/Sub...")
        self.subscriber.subscribe(self.subscription_path, callback=self.callback)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Stopped listening for messages.")