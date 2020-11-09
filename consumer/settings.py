##################################################
#       consumer   Settings File
##################################################

import os

CONSUMER_CONFIG = {
    "PARAMS": {
        "bootstrap.servers": os.getenv("CONSUMER_SERVER", "localhost:9092"),
        "group.id": os.getenv("CONSUMER_GROUP_ID", "simulator_consumer")
    },
    "TOPICS": os.getenv("CONSUMER_TOPICS", "vera-rubin-simulator").strip().split(",")
}

STEP_CONFIG = {

}