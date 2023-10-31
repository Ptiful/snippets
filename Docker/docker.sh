------------------------------Docker------------------------------
docker login
docker build -t app .  (creates image)
docker run app (create container)
docker image ls
docker container ls (docker ps)
docker image rm
docker stop img/container
docker system df
docker container/image prune --force
docker tag getting-started YOUR-USER-NAME/getting-started
docker push YOUR-USER-NAME/getting-started