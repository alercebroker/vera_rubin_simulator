from apf.core.step import GenericStep
from apf.producers import KafkaProducer
import logging
import time
import sys


# https://goshippo.com/blog/measure-real-size-any-python-object/
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


class ProducerSimulator(GenericStep):
    """VeraRubinSimulator Description

    Parameters
    ----------
    consumer : GenericConsumer
        Description of parameter `consumer`.
    **step_args : type
        Other args passed to step (DB connections, API requests, etc.)

    """

    consumed = 0
    messages = []
    elapsed_time = 0
    start_time = 0
    process_time = 60

    def __init__(self, consumer=None, config=None, level=logging.INFO, **step_args):
        super().__init__(consumer, config=config, level=level)
        self.producer = KafkaProducer(self.config.get("PRODUCER_CONFIG", None))

        self.n_messages = int(config.get("MESSAGES", 10))
        self.exposure_time = float(config.get("EXPOSURE_TIME", 30))
        self.process_time = float(config.get("PROCESS_TIME", 60))
        self.key = config.get("KEY", "alertId")
        self.start_time = time.time()

    def produce(self):
        self.logger.info(f"Consumed {self.consumed}, producing")

        for message in self.messages:
            self.producer.produce(message, key=str(message[self.key]))

        self.logger.info(f"Message produced, waiting flush.")
        if type(self.producer) is KafkaProducer:
            self.producer.producer.flush()
        self.consumed = 0
        self.messages = []

        t1 = time.time()
        real_time = max([0, (self.exposure_time+self.process_time)-(t1-self.start_time)])
        self.logger.info(f"Sleeping for Exposure ({self.exposure_time}s), Process ({self.process_time}s) | Real Time {real_time:.3f}s")
        time.sleep(real_time)
        self.start_time = time.time()

    def check_timeout(self):
        now = time.time()
        elapsed = now - self.start_time
        if elapsed >= self.process_time:
            self.logger.info("Consume timeout, producing")
            self.produce()

    def execute(self, message):
        """self.check_timeout()
        self.messages.append(message)
        self.consumed += 1
        if self.consumed == self.n_messages:
            self.produce()"""
        self.producer.produce(message)
