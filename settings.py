##################################################
#       vera_rubin_simulator   Settings File
##################################################
import os
from VERA_RUBIN_SCHEMA import SCHEMA

CONSUMER_CONFIG = {
  "CLASS": "apf.consumers.AVROInfiniteConsumer",
  "DIRECTORY_PATH": os.getenv("AVRO_PATH", "data/"),
}

PRODUCER_CONFIG = {
    "TOPIC": os.getenv("PRODUCER_TOPIC", "vera-rubin-simulator"),
    "PARAMS": {
        'bootstrap.servers': os.getenv("PRODUCER_SERVER", "localhost:9092"),
    },
    "SCHEMA": SCHEMA
}

STEP_CONFIG = {
    "PRODUCER_CONFIG": PRODUCER_CONFIG,
}
