FROM alpine:latest

RUN apk add --no-cache git make musl-dev go

# Configure Go
ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN go get -u github.com/golang/protobuf/protoc-gen-go

RUN apk add --update nodejs npm

# install simple http server for serving static content
RUN npm install -g http-server

#FROM namely/protoc-all
RUN apk add protobuf
RUN apk add curl wget

RUN /sbin/apk add --no-cache python2 && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache
#FROM python:2.7-slim
# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

# make the 'app' folder the current working directory
WORKDIR /app
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY package-lock.json .

COPY protoc-gen-grpc-web .
RUN chmod +x protoc-gen-grpc-web
RUN cp protoc-gen-grpc-web /sbin

COPY ./backend ./backend

COPY ./proto ./proto
RUN mkdir -p backend/proto
RUN mkdir -p frontend/proto
RUN protoc -I proto proto/*.proto --proto_path=./proto --go_out=plugins=grpc:./backend/proto
RUN protoc -I proto proto/*.proto --js_out=import_style=commonjs:./frontend/proto --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./frontend/proto

COPY ./frontend ./frontend

EXPOSE 8081
EXPOSE 9000

#WORKDIR /app/backend
#RUN go run main.go &

WORKDIR /app/frontend
# install project dependencies
RUN npm i -g @quasar/cli
RUN npm i

#RUN quasar dev
RUN /bin/sh

