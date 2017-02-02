FROM resin/rpi-raspbian:jessie

COPY src/packingdesk.py /usr/bin/packingdesk.py

ENTRYPOINT ["python /usr/bin/packingdesk.py"]