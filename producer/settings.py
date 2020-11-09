##################################################
#       producer   Settings File
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
        'message.max.bytes': 8000000
    },
    "SCHEMA": SCHEMA
}

STEP_CONFIG = {
    "PRODUCER_CONFIG": PRODUCER_CONFIG,
    "MESSAGES": os.getenv("MESSAGES", 10),
    "EXPOSURE_TIME": os.getenv("EXPOSURE_TIME", 30),
    "PROCESS_TIME": os.getenv("PROCESS_TIME", 60),
}
