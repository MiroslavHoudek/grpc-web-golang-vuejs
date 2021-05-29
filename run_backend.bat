SET CURRENTDIR="%cd%"
docker run --mount type=bind,source=%CURRENTDIR%\backend-python\,target=/app/backend/src --mount type=bind,source=%CURRENTDIR%\proto,target=/app/backend/proto -p 8081:8081 -it grpc-backend-python
