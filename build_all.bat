#!/bin/sh
docker build -f Dockerfile.python . -t grpc-backend-python
docker build -f Dockerfile.envoy -t grpc-envoy .
docker build -f Dockerfile.frontend -t grpc-frontend .