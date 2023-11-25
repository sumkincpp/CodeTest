#!/usr/bin/env bash

set -euo pipefail

# armv6l
# x86_64
ARCH=$(uname -m)
VERSION=$(curl -s https://go.dev/VERSION?m=text | head -1)

if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" = "aarch64" ]; then
    ARCH="arm64"
fi

wget -O go.tar.gz "https://go.dev/dl/${VERSION}.linux-$ARCH.tar.gz"
sudo tar -C /usr/local -xzf go.tar.gz
rm go.tar.gz

echo "Go ${VERSION} has been installed successfully."

# echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc && source ~/.bashrc
