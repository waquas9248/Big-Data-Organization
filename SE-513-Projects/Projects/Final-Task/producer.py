from kafka import KafkaProducer
from time import sleep
import requests
import json

# Coinbase API endpoint
bitURL = 'https://api.coinbase.com/v2/prices/btc-usd/spot'
ethURL = 'https://api.coinbase.com/v2/prices/eth-usd/spot'

# Producing as JSON
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
        api_version=(3,4,0),
value_serializer=lambda m: json.dumps(m).encode('ascii'))

while(True):
    sleep(5)
    eth = ((requests.get(ethURL)).json())
    bit = ((requests.get(bitURL)).json())
    print("Price fetched")
    producer.send('quickstart-events', eth)
    producer.send('quickstart-events', bit)
    print("Price sent to consumer")