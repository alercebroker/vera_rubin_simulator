from apf.core.step import GenericStep
from apf.producers import KafkaProducer
import logging


class VeraRubinSimulator(GenericStep):
    """VeraRubinSimulator Description

    Parameters
    ----------
    consumer : GenericConsumer
        Description of parameter `consumer`.
    **step_args : type
        Other args passed to step (DB connections, API requests, etc.)

    """
    def __init__(self, consumer=None, config=None, level=logging.INFO, **step_args):
        super().__init__(consumer, config=config, level=level)
        self.producer = KafkaProducer(self.config.get("PRODUCER_CONFIG", None))

    def execute(self, message):
        self.producer.produce(message)
