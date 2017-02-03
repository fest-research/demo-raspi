FROM fest/rpi-python-gpio


COPY src/packingdesk.py /usr/bin/packingdesk.py

ENTRYPOINT ["/usr/bin/python"]
CMD ["/usr/bin/packingdesk.py"]
