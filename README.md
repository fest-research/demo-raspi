
### IOT Demo

Demo iot application that simulates a logistics packing desk


### Deploy to Kubernetes

```shell
$ kubectl create -f https://raw.githubusercontent.com/fest-research/demo-raspi/master/assets/packing-daemonset.yaml
```

### Run from Source
```shell
sudo apt-get update && apt-get install -y \
    python \
    python-dev \
    python-rpi.gpio
python src/packingdesk.py 
```


### Travis

Travis CI [https://travis-ci.org/fest-research/demo-raspi]

