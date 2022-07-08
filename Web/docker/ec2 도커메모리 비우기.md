https://www.hahwul.com/2018/08/16/docker-no-space-left-on-device-in-macos/



Docker "No space left on device" 오류 해결 방법(in MacOS)


```

# 볼륨제거
echo "remote volumn"
docker volume rm $(docker volume ls -qf dangling=true)

# 이미지 제거
echo "remote docker images"
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
docker images -a | sed '1 d' | awk '{print $3}' | xargs -L1 docker rmi -f ```
