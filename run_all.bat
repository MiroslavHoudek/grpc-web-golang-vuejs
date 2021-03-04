SET CURRENTDIR="%cd%"
# Start envoy
docker run -p 9000:9000 -p 9001:9001 -it grpc-envoy
# Start Python backend
docker run --mount type=bind,source=%CURRENTDIR%\backend-python\,target=/app/backend/src --mount type=bind,source=%CURRENTDIR%\proto,target=/app/backend/proto -p 8081:8081 -it grpc-backend-python "python backend.py"
# Start Quasar frontend
docker run --mount type=bind,source=%CURRENTDIR%\frontend\src,target=/app/frontend/src -p 8080:8080 -it grpc-frontend