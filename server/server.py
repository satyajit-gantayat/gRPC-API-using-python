from concurrent import futures
import logging

import grpc
import forbes_pb2
import forbes_pb2_grpc

import mysql.connector as sqlconn
import os
import time

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("__Server__")

logger.info("Executing server.py...")

def get_dbConnection():
    while True:
        try:
            # db connection details
            host = "database"
            user = "root"
            dbname = "forbes"
            passwd = "root"
            port = "3306"
            
            logger.info(f"Got the following variables for db connection\n: user={user}, dbname={dbname}, passwd={passwd}")
            
            # establish db connection
            logger.info("connecting to the database...")
            conn = sqlconn.connect(user=user, password=passwd, host=host, port=port, database=dbname)
            
            return conn
        
        except Exception as e:
            logger.info("Waiting for database connection...")
            time.sleep(5)

class Forbes(forbes_pb2_grpc.ForbesServicer):
    def GetBillionaires(self, request, context):
        conn = get_dbConnection()
        logger.info("connected to the database...")
        cur = conn.cursor()
        
        query = "SELECT DISTINCT person_name, age, country, organization from forbes_billionaires"

        logger.info("querying the database...")
        cur.execute(query)
        rows = cur.fetchall()
        
        response = forbes_pb2.GetBillionairesResponse()
        
        for row in rows:
            billionaire = response.billionaires.add()
            billionaire.name = row[0]
            billionaire.age = row[1]
            billionaire.country = row[2]
            billionaire.organization = row[3]
        
        cur.close()
        conn.close()
        logger.info("Sending the result to client...")
        return response

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    forbes_pb2_grpc.add_ForbesServicer_to_server(Forbes(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    logger.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()