VERSION := "v0.2.0"

push:
    docker build --platform linux/amd64 \
    -t harbor.kymyth.com/library/nodriver-bench:latest \
    -t harbor.kymyth.com/library/nodriver-bench:{{VERSION}} \
    .
    docker push harbor.kymyth.com/library/nodriver-bench:latest
    docker push harbor.kymyth.com/library/nodriver-bench:{{VERSION}}
