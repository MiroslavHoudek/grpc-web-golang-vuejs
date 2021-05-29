SET CURRENTDIR="%cd%"
docker run --mount type=bind,source=%CURRENTDIR%\frontend\src,target=/app/frontend/src -p 8080:8080 -it grpc-frontend