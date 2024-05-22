from kafka import KafkaConsumer
from datetime import datetime
import json
import os
import pandas as pd
import numpy as np
from google.cloud import storage

os.environ['516778109899-compute@developer.gserviceaccount.com'] = r'/mnt/disks/se-413-375302-7cd244d5721a.json'
client = storage.Client()
bucket = client.get_bucket('schooldataset')

df = pd.DataFrame(columns = ['Base', 'Amount', 'Time'])

# Getting the data as JSON
consumer = KafkaConsumer('quickstart-events',
bootstrap_servers=['localhost:9092'],
api_version=(3,4,0),
value_deserializer=lambda m: json.loads(m.decode('ascii')))

for message in consumer:
    base = (message.value)['data']['base']
    price = (message.value)['data']['amount']

    data = {'Base': [base], 'Amount': [price], 'Time': [datetime.now()]}
    df2 = pd.DataFrame(data)

    df = pd.concat([df, df2])
    print('Message Recieved')
    bucket.blob("crypto_info.csv").upload_from_string(df.to_csv(index=False), 'text/csv')