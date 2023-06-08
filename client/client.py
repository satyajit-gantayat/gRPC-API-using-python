import time
import logging

import grpc
import forbes_pb2
import forbes_pb2_grpc

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("__Client__")

logger.info("Executing client.py...")

def wait_for_server():
    while True:
        try:
            # Attempt to establish a connection to the server
            with grpc.insecure_channel('server:50051') as channel:
                grpc.channel_ready_future(channel).result(timeout=5)
                logger.info("Server is ready and reachable...")
                break
        except Exception as e:
            logger.info("Waiting for the server...")
            time.sleep(5)

def run():
    wait_for_server()
    
    with grpc.insecure_channel('server:50051') as channel:
        stub = forbes_pb2_grpc.ForbesStub(channel)
        logger.info("Created server stub...")
        response = stub.GetBillionaires(forbes_pb2.GetBillionairesRequest())
        logger.info("Got some response from the stub...")
        logger.info("Printing server response...")
        for billionaire in response.billionaires:
            logger.info(f"{billionaire.name}, {billionaire.age}, {billionaire.country}, {billionaire.organization}")


if __name__ == '__main__':
    run()
