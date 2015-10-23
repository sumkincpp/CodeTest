docker rmi $(docker images -f "dangling=true" -q)

docker rm -v $(docker ps -a -q -f status=exited)
