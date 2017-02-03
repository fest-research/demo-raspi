FROM resin/rpi-raspbian:wheezy

# Install dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-rpi.gpio \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY src/packingdesk.py /usr/bin/packingdesk.py

ENTRYPOINT ["/usr/bin/python"]
CMD ["/usr/bin/packingdesk.py"]
