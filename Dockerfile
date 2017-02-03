FROM fest/rpi-python-gpio-min


COPY src/packingdesk.py /usr/bin/packingdesk.py

ENTRYPOINT ["/usr/bin/python"]
CMD ["/usr/bin/packingdesk.py"]
