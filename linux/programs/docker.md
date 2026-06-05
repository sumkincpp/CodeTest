# Docker notes

## Copying file from container to the host

docker cp <containerId>:/file/path/within/container /host/path/target

## Repushing docker images

```bash
copy_images() {
  local src_repo="$1"
  local dst_repo="$2"
  shift 2

  for name in "$@"; do
    docker pull "$src_repo/$name"
    docker tag "$src_repo/$name" "$dst_repo/$name"
    docker push "$dst_repo/$name"
  done
}

copy_images old-registry.com/myrepo new-registry.com/myrepo \
  app:latest api:v1 worker:v2
```
