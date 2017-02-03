FROM resin/rpi-raspbian:wheezy

RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-rpi.gpio \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*


