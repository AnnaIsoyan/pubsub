# pubsub
work with Google pub/sub messages

a simple subscriber receives pub/sub messages 
    stores in Google BigQuery
    stores in MongoDB /locally/

there is an example env file, build your .env file using it
1. create topic
2. create subscription
3. create service_account -> grant Cloud Pub/Sub service agent role, create key and download json
4. create a dataset and table in BigQuery. You must provide a schema
5. find client_email from your json file, go to BigQuery dataset, grant the principle BigQuery Data Editor and Viewer roles
6. copy env variable ids from gcp
7. run main.py script
8. go to pub/sub and publish a message
9. check results

