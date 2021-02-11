#!/bin/sh
python -m grpc_tools.protoc -I../proto --python_out=../src --grpc_python_out=../src ../proto/accounts.proto