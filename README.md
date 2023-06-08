### Introduction

This project explains how we can send/receive data using gRPC API.

The basic idea is as follows:
1. Send a request from client
2. Server should query the database after receiving the client request
3. Server should send the db query result back to the client

### Design idea

There are 3 different folders named `server`, `client` and `database`, each having its own Dockerfile. These 3 folders will be used to create 3 different docker containers.

There is a file `docker-compose.yml` which defines the container settings / services. It has 3 different services with relevant ports. The server container depends on the database container and the client depends on the server.

### Steps to test

1. Make sure that the protos files have been compiled and the compiled python files are there in the respective folders. If not, then compile them as described in the official documentation page.
https://grpc.io/docs/languages/python/quickstart/#generate-grpc-code

2. Make sure docker is installed and available in the terminal.

3. Navigate to the folder where you have the `docker-compose.yml` file. Run `docker-compose up` to build the containers and run the same.